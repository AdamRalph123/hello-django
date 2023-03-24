from django import forms
from .models import Item

class Itemform(forms.modelsform):
    class Meta:
        model = Item
        field = ['name', 'done']