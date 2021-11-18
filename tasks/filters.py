import django_filters
from django.utils.translation import ugettext as _

from tasks.models import Task


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ['status', 'assigned_to', 'lables']
        labels = {'status': _('Status'),
                  'assigned_to': _('Assigned to'),
                  'lables': _('Lable')}
