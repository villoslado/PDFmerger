from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("merge/", include("pdfmerger_app.urls")),  # Only include 'merge/' once here
]
