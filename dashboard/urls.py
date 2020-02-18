from django.urls import path
from .views import (DashboardView, KPIDetailView, Ibyakozwe, DistrictChartView,
                    SectorChartView, CreateFamily, AddKpi, load_cells, load_village, uploadImage, simple_upload, HomePageView, SearchResultsView)

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('kpi/<int:pk>', KPIDetailView.as_view(), name='kpi-detail'),
    path('ibyakozwe/<int:pk>', Ibyakozwe.as_view(), name='ibyakozwe'),
    path('ibisigaye/<int:pk>', Ibyakozwe.as_view(), name='ibisigaye'),
    path('ibyakozwe_sector/<int:pk>', Ibyakozwe.as_view(), name='ibyakozwe_sector'),
    path('ibisigaye_sector/<int:pk>', Ibyakozwe.as_view(), name='ibisigaye_sector'),
    path('kpi/charts/<int:pk>', DistrictChartView.as_view(), name='kpi_charts'),
    path('sector_chart/charts/<int:pk>', SectorChartView.as_view(), name='sector_charts'),
    path('add_family', CreateFamily.as_view(), name='family'),
    path('add_kpi', AddKpi.as_view(), name='add_kpi'),
    path('status/<int:pk>', uploadImage, name='status_change'),
    path('import/', simple_upload, name='import'),
    path('search/', HomePageView.as_view(), name='search'),
    path('search/results/', SearchResultsView.as_view(), name='search_results'),
    path('ajax/load-cells/', load_cells, name='ajax_load_cells'),
    path('ajax/load-villages/', load_village, name='ajax_load_villages'),
]