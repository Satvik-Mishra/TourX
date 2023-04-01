from django import forms
from hackathon.models import Hackathon


class HackathonCreateForm(forms.ModelForm):
    class Meta:
        model = Hackathon
        fields = ['name', 'description', 'logo', 'start_date', 'end_date',
                  'max_members', 'min_members', 'address', 'mode']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
