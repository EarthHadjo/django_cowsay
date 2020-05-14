from django import forms
from .models import CowText


class AddCowText(forms.ModelForm):
    class Meta:
        model = CowText
        fields = ('text',)
