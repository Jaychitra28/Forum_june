from django.forms import ModelForm

from ..models.response import Response
# from django.db import models
from ..models.thread import Thread


class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = ['title','description']
        # widgets = {'title':TextInput(attrs={'class':'form-control', 'placeholder':'Add thread'})}


class EditThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = ['title','description']

class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ['message']
        
        
        
class EditResponseForm(ModelForm):
    # message = CharField(label="My Message", widget=Textarea())
    class Meta:
        model = Response
        fields = ['message']

