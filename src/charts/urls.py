from django.urls import path

app_name = "charts"

urlpatterns = [
    path("charts/", ChartListView.as_view(), name="charts"),
]
