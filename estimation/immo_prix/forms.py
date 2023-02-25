from django.forms import ModelForm
from .models import Formu

class Formu_note_users(ModelForm):
   
   class Meta:
        model = Formu
        fields = '__all__'
        # fields = [ "client", ] 