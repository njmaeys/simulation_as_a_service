from django import forms

class NameForm(forms.Form):

    multiplier = forms.CharField(label='Multiplier', max_length=100)
