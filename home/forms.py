from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Experience

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
        widgets = {
            'start_date': AdminDateWidget(),
            'end_date': AdminDateWidget(),
        }