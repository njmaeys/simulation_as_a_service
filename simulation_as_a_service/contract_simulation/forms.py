from django import forms

class NameForm(forms.Form):

    ground = forms.CharField(label='Ground Disc', max_length=100)
    express = forms.CharField(label='Express Disc', max_length=100)
    international = forms.CharField(label='International Disc', max_length=100)
