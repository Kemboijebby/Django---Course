import django_filters
from .models import *
from django_filters import DateFilter

class OrderFilter(django_filters.FilterSet):

    start_data = DateFilter(field_name='date_created',lookup_expr ='gte')
    end_data = DateFilter(field_name='date_created',lookup_expr = 'lte')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']