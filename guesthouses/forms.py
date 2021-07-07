from django import forms
from . import models

class Searchform(forms.Form):

    city = forms.CharField(initial="제주시")
    price = forms.IntegerField(required=False)
    signatureType = forms.ModelMultipleChoiceField(required=False, queryset=models.SignatureType.objects.all(), widget=forms.CheckboxSelectMultiple)
