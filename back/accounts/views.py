import os
from django.forms import model_to_dict
from django.http import FileResponse, HttpResponse
from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib import messages
from django.core.files.storage import default_storage
from accounts.models import User
from accounts.forms import UserRegisterForm, UserProfileForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Your account has been created. You can log in now!"
            )
            return redirect("login")
        else:
            print(form.errors)
            return redirect("login")
    else:
        form = UserRegisterForm()
        context = {"form": form}
        return render(request, "accounts/register.html", context)


def profile(request):
    user = request.user
    context = {}
    if user:
        #if user.resume:
        #    file_path = user.resume.url
        #    file_name = os.path.basename(file_path)
        #with open(file_path, 'rb') as file:
        #    response = HttpResponse(file.read(), content_type='application/octet-stream')
        #    response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        #context['response'] = response
        #response = HttpResponse(user.resume.read(), content_type='application/pdf')
        #response['Content-Disposition'] = 'attachment; filename="{}"'.format(user.resume.name)
        context = model_to_dict(user)
        #context['resume'] = response
    else:
        context["message"] = "You are not logged in"
    return render(request, "accounts/profile.html", context)

def edit_profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES)
        print(form.data)
        if form.is_valid():
            user = User.objects.filter(id=request.user.id)
            if user.count() == 1:
                print(form.cleaned_data)
                data = form.cleaned_data
                print(request.FILES)
                resume = request.FILES.get('resume')
                if resume:
                    user[0].resume.save(resume.name, resume)
                    resume_file = form.cleaned_data['resume'].file
                    with open(os.path.join(settings.MEDIA_ROOT, resume.name), 'wb') as f:
                        f.write(resume_file.getbuffer())
                    print(resume_file)

                user.update(**data)
            messages.success(
                request, f"Your profile has been updated."
            )
            return redirect("profile")
        else:
            print(form.errors)
            return redirect("login")
    else:
        user = request.user
        form = UserProfileForm(instance=user)
        context = {"form": form}
        return render(request, "accounts/profile_edit.html", context)


