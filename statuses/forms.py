from django.forms import ModelForm
from django.utils.translation import ugettext as _

from .models import TaskStatus


class StatusForm(ModelForm):
    class Meta:    
        model = TaskStatus
        fields = ('name',) 
        labels = {'name': _('Name'),}  
