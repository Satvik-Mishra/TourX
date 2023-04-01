from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("accounts.urls")),
    path("", TemplateView.as_view(template_name='base.html'), name='home'),
    path("hacks/", include("hackathon.urls")),
]
