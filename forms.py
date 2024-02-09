from django import forms
from .models import BackgroundImage

class BackgroundImageForm(forms.ModelForm):
    class Meta:
        model = BackgroundImage
        fields = ['image']
