from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from hackathon.views import list_hackathons

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("accounts.urls")),
    # path("", TemplateView.as_view(template_name='base.html'), name='home'),
    path("", list_hackathons, name="home"),
    path("hacks/", include("hackathon.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
