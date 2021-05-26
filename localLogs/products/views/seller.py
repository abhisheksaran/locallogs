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
from ..models import User, Items
from ..decorators import seller_required
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
        return redirect('seller:items_change_list')

@method_decorator([login_required, seller_required], name='dispatch')
class ItemsListView(ListView):
    model = Items
    ordering = ('name',)
    context_object_name = 'items'
    template_name ='products/seller/items_home_list.html'

    def get_query(self):
        queryset = self.request.user.items
        return queryset
    

class ItemsAddView(UpdateView):
    model = Items
    fields = ('name', 'category', 'description','tags', )
    template_name = 'products/seller/item_add_form.html'

    def form_valid(self, form):
        quiz = form.save(commit=False)
        quiz.owner = self.request.user
        quiz.save()
        messages.success(self.request, 'The the item is added successfully')
        return redirect('seller:items_list')

class ItemUpdateView():
    model = Items
    fields = ('name', 'subject', )
    context_object_name = 'items'
    template_name = 'classroom/teachers/item_update_form.html'

   
class ProductDeleteView():
    pass

def product_add():
    pass

def product_change():
    pass

class ProductDeleteView():
    pass