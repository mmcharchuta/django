from django.urls import path

from . import views

app_name = "weather"

urlpatterns = [
    path("", views.index_view, name="index"),
    path("<source>", views.index_view, name="index"),
]
