from django import forms
from localflavor.in_.forms import INZipCodeField
from .models import Order

class OrderCreateForm(forms.ModelForm):
    postal_code = INZipCodeField()
    class Meta:
        model = Order   
        fields = ['first_name', 'last_name', 'email', 'address','postal_code', 'city']