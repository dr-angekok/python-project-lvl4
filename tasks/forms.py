from django.contrib.auth.models import User
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

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['executor'].queryset = User.objects.all()
        self.fields['executor'].label_from_instance = lambda obj: "%s %s" % (obj.first_name, obj.last_name)
