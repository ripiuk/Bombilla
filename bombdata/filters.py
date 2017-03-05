import django_filters
from .models import Object


class ObjectFilter(django_filters.FilterSet):
    filling = django_filters.CharFilter(name='filling', lookup_type='icontains')

    class Meta:
        model = Object
        fields = ['id', 'filling']