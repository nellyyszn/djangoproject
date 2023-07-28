from django import forms
from school.models import student


class studentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name','course','admission']


