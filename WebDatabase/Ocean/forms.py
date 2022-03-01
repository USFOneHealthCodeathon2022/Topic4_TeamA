from django.forms import ModelForm, widgets
from .models import Ocean
from django import forms

class HomeForm(forms.Form):
     search=forms.CharField(max_length=200)

#class HomeForm(ModelForm):
     
#     class Meta:
#         model = Codeathon
#         fields = ['accession', 'species', 'genus', 'family', 'genebanktitle']
         
     #email_notice = forms.BooleanField(required=False)
     #user_email=forms.EmailField(max_length=200)


class EmailForm(forms.Form):
     email=forms.EmailField(max_length=200)
