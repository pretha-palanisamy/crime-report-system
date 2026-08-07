from django import forms
from .models import Crime

class CrimeForm(forms.ModelForm):
    class Meta:
        model = Crime
        fields = ['crime_type', 'description', 'location']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }