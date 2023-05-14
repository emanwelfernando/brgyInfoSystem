from django.forms import ModelForm
from .models import *

class residentForm(ModelForm):
    class Meta:
        model = Resident
        fields = '__all__'