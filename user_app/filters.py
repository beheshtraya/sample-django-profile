import django_filters
from django_filters import rest_framework as filters

from user_app.models import Profile


class ProfileFilter(filters.FilterSet):
    birthday_after = django_filters.DateFilter(label='birthday_after', method='birthday_after_filter')

    class Meta:
        model = Profile
        fields = ['birthday_after']

    def birthday_after_filter(self, queryset, name, value):
        return queryset.filter(birthday__gt=value)

