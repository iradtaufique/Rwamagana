from django.shortcuts import render
from django.views.generic import ListView

from agriculture.models import Crops, Seeds


class AgricultureListView(ListView):
    model = Crops
    template_name = "agriculture/agriculture_details.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AgricultureListView, self).get_context_data(**kwargs)
        context['crops'] = Crops.objects.all()
        context['seeds'] = Seeds.objects.all()
        # context['achieved_results'] = Result.objects.filter(achieved=0, sector=self.request.user.user_profile.sector)
        # context['pending_results'] = Result.objects.filter(pending=0, sector=self.request.user.user_profile.sector)
        # context['sectors'] = Sector.objects.all()
        # # context['results_by_kpi'] = Result.objects.all().filter(kpi_id=self.kwargs['kpi_id'])
        # context['achieved_total'] = Result.objects.values('kpi__name', 'kpi_id').annotate(achieved=Sum('achieved')).annotate(pending=Sum('pending'))

        return context
