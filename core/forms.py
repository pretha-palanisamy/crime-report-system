from django import forms
from .models import Crime

class CrimeForm(forms.ModelForm):
    class Meta:
        model=Crime
        fields='__all__'
        exclude=['reported_by']
        widgets={
            'date_time':forms.DateTimeInput(attrs={'type':'datetime-local'})
        }