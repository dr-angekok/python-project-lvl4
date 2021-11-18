from django.forms import ModelForm
from django.utils.translation import ugettext as _

from .models import TaskLable, TaskStatus, Task


class StatusForm(ModelForm):
    class Meta:    
        model = TaskStatus
        fields = ('name',) 
        labels = {'name': _('Name'),}  


class LableForm(ModelForm):
    class Meta:    
        model = TaskLable
        fields = ('name',) 
        labels = {'name': _('Name'),}
