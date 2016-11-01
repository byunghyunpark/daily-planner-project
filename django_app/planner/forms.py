from django import forms

from .models import Schedule


class ScheduleAddForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = ('name', 'plan_start', 'plan_finish')