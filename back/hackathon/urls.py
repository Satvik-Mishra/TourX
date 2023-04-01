from django.urls import path

from hackathon.views import create_hackathon, list_hackathons, index_hackathon

urlpatterns = [
    path("create/", create_hackathon, name="create-hack"),
    path("list/", list_hackathons, name='list-hacks'),
    path("<int:pk>/", index_hackathon, name='index-hackathon'),
]
