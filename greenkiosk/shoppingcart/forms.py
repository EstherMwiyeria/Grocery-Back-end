from django import forms
from .models import ShoppingCart

class ShoppingUploadForm(forms.ModelForm): 
    
    class Meta:
        # defines the model
        model = ShoppingCart
        # renders all the fields in the form
        fields = "__all__"

        


