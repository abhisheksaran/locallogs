from django.shortcuts import render
from django.contrib import messages
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
    

class ItemsAddView(CreateView):
    model = Items
    fields = ('name', 'category', 'description' )
    template_name = 'products/seller/item_add_form.html'

    def form_valid(self, form):
        item = form.save(commit=False)
        item.owner = self.request.user
        item.save()
        messages.success(self.request, 'The the item is added successfully')
        return redirect('seller:items_list')

# def item_add(request):
#     items = get_object_or_404(Items, owner=request.user)
#     if request.method == 'POST':
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             item = form.save(commit=False)
#             item.owner = self.request.user
#             item.save()
#             messages.success(request, 'Item has been added successfully')
#             return redirect ('seller:items_list')
#     else form = QuestionForm()

#     return render(request, 'products/seller/item_add_form.html',{'items':items, 'form':form})


class ItemUpdateView():
    pass

   
class ProductDeleteView():
    pass

def product_add():
    pass

def product_change():
    pass

class ProductDeleteView():
    pass