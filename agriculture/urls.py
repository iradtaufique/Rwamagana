from django.urls import path, include
from .views import AgricultureListView

urlpatterns = [
    path('crops', AgricultureListView.as_view(), name='crops'),
    path('seeds', AgricultureListView.as_view(), name='seeds'),
]