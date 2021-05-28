from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from products.models import User

class SellerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'contact_number', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_seller = True
        if commit:
            user.save()
        return user


class BuyerSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'contact_number', 'password1', 'password2']
        
    
    def save(self,commit= True):
        user = super().save(commit=False)
        user.is_buyer = True
        if commit: 
            user.save()
        return user
