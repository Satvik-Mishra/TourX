from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model= User
        widgets = {
            "graduation_completion": forms.DateInput(
                attrs={'type': 'date'}
                ),
        }
        fields = ['username', 'email', 'password', 'first_name', 
              'last_name', 'college_name', 'graduation_completion',
              'address', 'city', 't_shirt_size', 'linkedin_url', 'github_url', 
         ]
