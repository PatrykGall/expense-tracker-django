from django import forms

from .models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["category", "amount", "date", "description"]
        widgets = {
            "category": forms.Select(attrs={"class": "form-select"}),
            "amount": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
        }
        labels = {
            "category": "Kategoria",
            "amount": "Kwota",
            "date": "Data",
            "description": "Opis",
        }