from django.urls import path
from .views import merge_view

urlpatterns = [
    path("", merge_view, name="merge_view"),
]
