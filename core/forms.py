from .models import company
from django import forms

class companyform(forms.ModelForm):
    class Meta:
        model=company
        fields = "__all__"