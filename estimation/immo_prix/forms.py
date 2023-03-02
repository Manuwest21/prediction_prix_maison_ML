from django.forms import ModelForm
from .models import Formu, Champs
from django import forms


class Formu_note_users(ModelForm):
   
   class Meta:
        model = Formu
        fields = '__all__'
        # fields = [ "client", ] 
        
class ContactUsForm(forms.Form):
   name = forms.CharField(required=False)    #required=False >>> signifie que le champ n'est aps indispensablement requis!
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)
   
   
class Ask_logement(ModelForm):
   
   class Meta:
      model= Champs 
      exclude = ['estimation_prix']
      
      
