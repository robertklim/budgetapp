from django import forms

class ExpenseForm(forms.Form):
    name = forms.CharField()
    amount = forms.CharField()
    category = forms.CharField()