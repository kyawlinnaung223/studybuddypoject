from django.forms import ModelForm      
from .models import Room

class RoomCreateForm(ModelForm):
          class Meta:
                    model=Room
                    fields='__all__'
                    exclude=['user','participants']