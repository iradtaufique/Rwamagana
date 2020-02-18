from django.contrib import messages
from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View, CreateView, TemplateView

from tablib import Dataset

from .forms import FamilyForm, AddKpiForm, UploadImage
from .models import Sector, KPI, Umuryango, Cell, Village
from django.db.models import Sum, Count, F, Q
from .import forms
from .resources import UmuryangoResource



class DashboardView(ListView):
    model = Umuryango
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['kpis'] = KPI.objects.all()
        context['sectors'] = Sector.objects.all()
        context['achieved_total'] = Umuryango.objects.values('kpi__name', 'kpi_id') \
                                                     .annotate(achieved=Sum('achieved')) \
                                                     .annotate(target=Sum('target'))

        context['achieved_sector'] = Umuryango.objects.values('kpi__name', 'kpi_id')\
                                                  .annotate(achieved=Sum('achieved'))\
                                                  .annotate(target=Sum('target'))\
                                                #   .filter(sector=self.request.user.user_profile.sector)

        return context


class KPIDetailView(DetailView):
    model = KPI
    template_name = "dashboard/kpi_detail.html"

    def get_context_data(self, **kwargs):
        context = super(KPIDetailView, self).get_context_data(**kwargs)
        context['kpis'] = KPI.objects.all()
        context['current_kpi'] = Umuryango.objects.filter(kpi_id=self.kwargs['pk'])\
                                          .values('kpi__name').annotate(targ=Sum('target'))\
                                          .annotate(achiev=Sum('achieved'))\
                                          .distinct()
        context['kpiname'] = Umuryango.objects.values('kpi__name').filter(kpi_id=self.kwargs['pk'])

        return context


class Ibyakozwe(ListView):
    model = KPI
    template_name = "umuryango/ibyakozwe.html"

    def get_context_data(self, **kwargs):
        context = super(Ibyakozwe, self).get_context_data(**kwargs)
        context['ibyakozwe'] = Umuryango.objects.filter(achieved=1).filter(kpi_id=self.kwargs['pk'])
        context['ibisigaye'] = Umuryango.objects.filter(achieved=0).filter(kpi_id=self.kwargs['pk'])

        context['ibyakozwe_sector'] = Umuryango.objects.filter(achieved=1, sector=self.request.user.user_profile.sector)\
                                                       .filter(kpi_id=self.kwargs['pk'])
        context['ibisigaye_sector'] = Umuryango.objects.filter(achieved=0, sector=self.request.user.user_profile.sector)\
                                                       .filter(kpi_id=self.kwargs['pk'])

        return context


# --------------------- view for District chart -----------------------------------#
class DistrictChartView(View):
    def get(self, request, pk):
        dataset = Umuryango.objects.values('kpi__name', 'sector__name').annotate(targ=Sum('target')) \
                           .annotate(achiev=Sum('achieved'))\
                           .filter(kpi_id=self.kwargs['pk'])\
                           .order_by('target')

        return render(request, 'dashboard/kpi_detail.html', {'dataset': dataset})


# --------------------- view for sector chart -----------------------------------#
class SectorChartView(View):
    def get(self, request, pk):
        dataset = Umuryango.objects.values('kpi__name', 'sector__name').annotate(targ=Sum('target')) \
                           .annotate(achiev=Sum('achieved')) \
                           .filter(kpi_id=self.kwargs['pk']) \
                           .filter(sector=self.request.user.user_profile.sector) \
                           .order_by('target')

        return render(request, 'dashboard/kpi_detail.html', {'dataset': dataset})


# --------------------- view for add new family -----------------------------------#
class CreateFamily(CreateView):
    model = Umuryango
    form_class = FamilyForm
    template_name = 'umuryango/add_data_form.html'

    def form_valid(self, form):
        fam = form.save(commit=False)
        fam.save()
        messages.success(self.request, 'Family  created successfully.')
        return redirect('dashboard')


#-----------------------view for loading cells based sector ----------------------#
def load_cells(request):
    sector_id = request.GET.get('sector')
    cells = Cell.objects.filter(sector_id=sector_id).order_by('name')
    return render(request, 'dashboard/dropdown.html', {'cells': cells})


#----------------------view for loading village Based on cells ------------------#
def load_village(request):
    cell_id = request.GET.get('cell')
    villages = Village.objects.filter(cell_id=cell_id).order_by('name')
    return render(request, 'dashboard/dropdown.html', {'villages': villages})


# --------------- view for adding KPI on the frontend ---------------------------#
class AddKpi(CreateView):
    model = KPI
    form_class = AddKpiForm
    template_name = 'umuryango/add_data_form.html'

    def form_valid(self, form):
        kpiform = form.save(commit=False)
        kpiform.save()
        messages.success(self.request, 'KPI created successfully.')
        return redirect('dashboard')


# ----------------view for uploading and changing status to 1 or true ---------------#
def uploadImage(request, pk):
    post = get_object_or_404(Umuryango, pk=pk)
    if request.method == "POST":
        form = UploadImage(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post.save()
            Umuryango.objects.filter(sector=request.user.user_profile.sector, pk=pk).update(achieved=1)
            messages.success(request, 'Status changed successfully')
            return redirect('dashboard')
    else:
        form = UploadImage(instance=post)
    return render(request, 'umuryango/change_status.html', {'form': form})


# -------------- Upload csv file --------------------------#
def simple_upload(request):

    import tablib
    if request.method == 'POST':
        umuryango_resource = UmuryangoResource()
        dataset = tablib.Dataset()
        new_umuryangos = request.FILES['file']

        imported_data = dataset.load(new_umuryangos.read(), format('xlsx'))
        result = umuryango_resource.import_data(dataset, dry_run=True)

        if not result.has_errors():
            umuryango_resource.import_data(dataset, dry_run=False)
            messages.success(request, 'Your data has been Imported succesfuly !!')
            return redirect('dashboard')

        else:
            messages.error(request, 'there is an error during importing xlsx file]')
            return redirect('dashboard')

    return render(request, 'umuryango/import.html')


class HomePageView(TemplateView):
    template_name = 'dashboard/home.html'

class SearchResultsView(ListView):
    model = Umuryango
    template_name = 'dashboard/results.html'

    
    def get_queryset(self, *args, **kwargs): 
        query1 =  self.request.GET.get('forsector')
        query2 =  self.request.GET.get('forkpi')
        
        object_list = Umuryango.objects.filter(
            Q(sector__name__icontains=query1) & Q(kpi__name__icontains=query2)
            ).values('kpi__name', 'sector__name','kpi_id') \
                     .annotate(achieved=Sum('achieved')) \
                     .annotate(target=Sum('target'))
        return object_list

  
