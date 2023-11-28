from django import forms
from apps.schedule.models import schedule, schedule_category
import re

class ScheduleForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=schedule_category.objects.all(), widget=forms.Select())
    class Meta:
        model = schedule
        fields = ['first_name','last_name','email', 'phone', 'description', 'category']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'phone': 'Phone',
            'description': 'Description',
            'category': 'Category',
        }

    def clean_phone(self):
        data = self.cleaned_data['phone'].strip()

        pattern = r'^[0-9]+$'

        if not re.match(pattern, data):
            raise forms.ValidationError('Must contain only numeric characters.')
        
        return data