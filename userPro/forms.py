from django import forms

class searchForm(forms.Form):
    q = forms.CharField()

class AddForm(forms.Form):
    a = forms.CharField()
    b = forms.CharField()