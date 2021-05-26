from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect,render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator 
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)

from ..forms import SellerSignUpForm, BuyerSignUpForm
from ..models import User
# Create your views here.


class SellerSignUpView(CreateView):
    model = User
    form_class = SellerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'seller'
        return super().get_context_data(**kwargs)

    def from_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('seller:product_change_list')


class ProductListView():
    pass

class ProductCreateView():
    pass

class ProductUpdateView():
    pass

class ProductDeleteView():
    pass

def product_add():
    pass

def product_change():
    pass

class ProductDeleteView():
    pass