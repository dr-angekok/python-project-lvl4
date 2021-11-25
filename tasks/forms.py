from django.forms import ModelForm
from django.utils.translation import ugettext as _

from .models import Task


class  TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'content', 'status', 'executor', 'labels')
        labels = {
            'name': _('Name'),
            'content': _('content'),
            'status': _('status'),
            'executor': _('assigned_to'),
            'labels': _('labels')
        }
