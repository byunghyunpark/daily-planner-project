from django import forms

from .models import Schedule


class ScheduleAddForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = ('name', )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }