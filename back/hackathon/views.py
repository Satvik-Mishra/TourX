import datetime

from django.shortcuts import get_object_or_404, redirect, render
from hackathon.models import Hackathon
from hackathon.forms import HackathonCreateForm

def create_hackathon(request):
    print(request.user.is_superuser)
    if request.method == 'POST' and request.user.is_superuser:
        form = HackathonCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.created_by_id = request.user.id
            hackathon = form.save()
            redirect('list-hacks')
        else:
            pass
    else:
        form = HackathonCreateForm()
    return render(request, 'hackathon/create.html', {'form': form})

def list_hackathons(request):
    is_superuser = request.user.is_superuser
    context = {}
    if is_superuser:
        hackathons = Hackathon.objects.filter(
            created_by = request.user.id
         )
        previous_hackathons = Hackathon.objects.filter(
            created_by = request.user.id,
            end_date__lt = datetime.datetime.now(),
        )
    else:
        hackathons = Hackathon.objects.filter(start_date__gt=datetime.datetime.now())
        previous_hackathons = Hackathon.objects.filter(end_date__lt=datetime.datetime.now())
    context['hacks'] = hackathons
    context['previous_hacks'] = previous_hackathons
    return render(request, 'hackathon/list.html', context)


def index_hackathon(request, pk):
    hackathon = get_object_or_404(Hackathon, id=pk)
    context = {}
    context['hack'] = hackathon
    return render(request, 'hackathon/index.html', context)
