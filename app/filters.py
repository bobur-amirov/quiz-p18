import django_filters
from django import forms

from .models import Result


class ResultFilter(django_filters.FilterSet):
    score_gt = django_filters.NumberFilter(field_name='score', lookup_expr='gt')
    score_lt = django_filters.NumberFilter(field_name='score', lookup_expr='lt')
    start_date = django_filters.DateFilter(field_name='created_at', lookup_expr='gte',
                                           widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = django_filters.DateFilter(field_name='created_at', lookup_expr='lt',
                                         widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Result
        fields = ['user__phone', 'score_gt', 'score_lt']
