from django.forms import ModelForm
from .models import *
from django import forms

class residentForm(ModelForm):
    class Meta:
        model = Resident
        fields = '__all__'