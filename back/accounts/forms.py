from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        widgets = {
            "graduation_completion": forms.DateInput(attrs={"type": "date"}),
        }
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "college_name",
            "graduation_completion",
            "address",
            "city",
            "t_shirt_size",
            "linkedin_url",
            "github_url",
            "resume",
        ]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            "graduation_completion": forms.DateInput(attrs={"type": "date"}),
            "resume": forms.FileInput(),
        }
        fields = [
            "first_name",
            "last_name",
            "college_name",
            "graduation_completion",
            "address",
            "city",
            "t_shirt_size",
            "linkedin_url",
            "github_url",
            "resume",
        ]
        enctype = "multipart/form-data"
