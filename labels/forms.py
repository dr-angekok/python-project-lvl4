from django.forms import ModelForm
from django.utils.translation import ugettext as _

from .models import TaskLabel

class LabelForm(ModelForm):
    class Meta:    
        model = TaskLabel
        fields = ('name',) 
        labels = {'name': _('Name'),}