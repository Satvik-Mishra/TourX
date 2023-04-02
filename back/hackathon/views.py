import datetime
from django.http import JsonResponse

from PyPDF2 import PdfReader

from django.shortcuts import get_object_or_404, redirect, render
from hackathon.models import Hackathon, Team
from hackathon.forms import HackathonCreateForm, TeamCreateForm, TeamJoinForm


def create_hackathon(request):
    if request.method == "POST" and request.user.is_superuser:
        form = HackathonCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.created_by_id = request.user.id
            hackathon = form.save()
            redirect("list-hacks")
        else:
            pass
    else:
        form = HackathonCreateForm()
    return render(request, "hackathon/create.html", {"form": form})


def create_team(request, pk):
    if request.method == "POST":
        form = TeamCreateForm(request.POST)
        if form.is_valid():
            team = form.save()
            team.member.add(request.user)
            print(team.__dict__)
            if team:
                hackathon = Hackathon.objects.filter(id=pk).first()
                if hackathon:
                    hackathon.teams.add(team)
                    redirect("index-hackathon", pk=pk)
        else:
            pass
    else:
        form = TeamCreateForm()
    return render(request, "team/create.html", {"form": form})


def join_team(request, pk):
    if request.method == "POST":
        form = TeamJoinForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print(form.instance.code)
            team = Team.objects.filter(code=form.instance.code).first()
            print(team)
            if team:
                team.member.add(request.user)
                hackathon = Hackathon.objects.filter(id=pk).first()
                if hackathon:
                    print(hackathon.teams.all())
                    hackathon.teams.add(team)
                    print(hackathon.teams.all())
                    redirect("index-hackathon", pk=pk)
            else:
                # TODO: NO TEAM EXISTS
                pass
        else:
            pass
    else:
        form = TeamJoinForm()
    return render(request, "team/join.html", {"form": form})


def list_hackathons(request):
    is_superuser = request.user.is_superuser
    context = {}
    if is_superuser:
        hackathons = Hackathon.objects.filter(created_by=request.user.id)
        previous_hackathons = Hackathon.objects.filter(
            created_by=request.user.id,
            end_date__lt=datetime.datetime.now(),
        )
    else:
        hackathons = Hackathon.objects.filter(start_date__gt=datetime.datetime.now())
        previous_hackathons = Hackathon.objects.filter(
            end_date__lt=datetime.datetime.now()
        )
    context["hacks"] = hackathons
    context["previous_hacks"] = previous_hackathons
    return render(request, "hackathon/list.html", context)


def index_hackathon(request, pk):
    hackathon = get_object_or_404(Hackathon, id=pk)
    user = request.user
    if hackathon:
        print(hackathon)
        for team in hackathon.teams.all():
            print(team)
            members = team.member.all()
            print(members)
            if user in members:
                print(user)
                return redirect('index-team', pk=team.id)
    context = {}
    context["hack"] = hackathon
    return render(request, "hackathon/index.html", context)

def index_team(request, pk):
    team = get_object_or_404(Team, id=pk)
    context = {}
    context["team"] = team 
    context["members"] = team.member.all()
    return render(request, "team/index.html", context)

def keyword_rater(request, pk):
    user = request.user
    if request.method == "POST" and user.is_superuser:
        keywords = request.POST["keywords"]
        keywords = [k.lower() for k in keywords.split()]
        hackathon = get_object_or_404(Hackathon, id=pk)
        all_teams = hackathon.teams.all()
        user_ratings = []
        for team in all_teams:
            users = team.member.all()
            print(users)
            for user in users:
                resume = user.resume
                print(user.resume)
                if resume:
                    reader = PdfReader(resume)
                    page = reader.pages[0]
                    text = page.extract_text()
                    total_kw = len(keywords)
                    total_tx = len(text)
                    match = 0
                    print(keywords)
                    matched_kw = set()
                    text = [t.lower() for t in text.split()]
                    print(text)
                    for t in text:
                        if t in keywords:
                            print(t)
                            match += 1
                            matched_kw.add(t)
                    print(matched_kw)
                    rating = len(matched_kw) / total_kw * 10
                    print(rating)
                    fraud_rating = total_kw / total_tx * 100
                    if fraud_rating in range(80, 100):
                        rating = 0.1
                    user.keyword_rating = rating 
                    user_ratings.append(user.keyword_rating)
                    user.save()
            return JsonResponse(
                    {'ratings': user_ratings}, safe=False
                    )
    else:
        return render(request, "hackathon/keyword_rater.html")

                
