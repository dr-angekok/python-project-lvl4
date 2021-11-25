import django_filters
from django.utils.translation import ugettext as _

from tasks.models import Task


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']
        labels = {'status': _('Status'),
                  'executor': _('Assigned to'),
                  'labels': _('Label')}
