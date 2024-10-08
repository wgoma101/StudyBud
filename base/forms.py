from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        exclude = ['host', 'participants'] # exclude these fields from the form
