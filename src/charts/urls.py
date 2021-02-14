from django.urls import path
from .views import ChartsListView

app_name = "charts"

urlpatterns = [
    path("", ChartsListView.as_view(), name="charts"),
]
