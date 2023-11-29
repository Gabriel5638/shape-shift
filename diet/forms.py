from django import forms
from django.core.exceptions import ValidationError
from .models import MealJournalEntry
from datetime import datetime, timedelta, date as py_date


class MealForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = MealJournalEntry
        fields = ['date', 'time', 'meal_type', 'meal']
        widgets = {
            'meal_type': forms.Select(choices=MealJournalEntry.MEAL_TYPES),
        }

    def clean_date(self):
        entered_date = self.cleaned_data['date']
        if entered_date > py_date.today():
            raise ValidationError("Please enter a date that is not in the future.")
        return entered_date

    def clean_time(self):
        entered_time = self.cleaned_data['time']
        now = datetime.now().time()
        # Checking if the entered time is in the future compared to the current time
        if entered_time > (datetime.combine(py_date.today(), now) + timedelta(minutes=1)).time():
            raise ValidationError("Please enter a time that is not in the future.")
        return entered_time
        
        
        
        
        
        
        
       