import django_filters
from .models import *

class ResidentFilters(django_filters.FilterSet):
    class Meta:
        name = django_filters.CharFilter(label='Full Name')
        model = Resident
        fields = ['name', 'age']