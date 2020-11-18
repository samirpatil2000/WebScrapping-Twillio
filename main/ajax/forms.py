from django import forms
from .models import Photo

class Form(forms.ModelForm):
    class Meta:
        model=Photo
        fields=('name','image')
