import django_filters
from django.utils.translation import ugettext as _

from tasks.models import Task


class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']

    def __init__(self, *args, **kwargs):
        super(TaskFilter, self).__init__(*args, **kwargs)
        self.filters['status'].label=_('Status')
        self.filters['executor'].label=_('Assigned to')
        self.filters['executor'].field.label_from_instance = lambda obj: "{} {}".format(obj.first_name, obj.last_name)
        self.filters['labels'].label=_('Label')
