from django import forms
from django.utils.translation import gettext_lazy as _

#select product quality choice from 1 to 2
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,coerce=int,label=_('Quantity'))
    # allows to indicate wheather the quantity has to be added to any existing quantity
    # hidden input this dont want to display to user
    override = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)
    
    