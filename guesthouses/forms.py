from django import forms
from . import models

class Searchform(forms.Form):

    city = forms.CharField(initial="제주시")
    price = forms.IntegerField(required=False)
    signature = forms.ModelMultipleChoiceField(required=False, queryset=models.Signature.objects.all(), widget=forms.CheckboxSelectMultiple)
