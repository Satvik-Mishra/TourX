from django.urls import path

from hackathon.views import (
    create_hackathon,
    index_team,
    list_hackathons,
    index_hackathon,
    create_team,
    join_team,
    keyword_rater,
)

urlpatterns = [
    path("create/", create_hackathon, name="create-hack"),
    path("", list_hackathons, name="list-hacks"),
    path("<int:pk>/", index_hackathon, name="index-hackathon"),
    path("<int:pk>/create-team/", create_team, name="create-team"),
    path("<int:pk>/join-team/", join_team, name="join-team"),
    path("<int:pk>/team/", index_team, name="index-team"),
    path('<int:pk>/keyword_rater/', keyword_rater, name='keyword-rater'),
]
