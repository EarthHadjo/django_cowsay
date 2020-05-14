from django import forms
from django.db import models
from Cowsay.models import Text


class Cow_Text(forms.Form):
    text = forms.CharField(label="text", max_length=60)
