from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

#from ..decorators import buyer_required
from ..forms import SellerSignUpForm, BuyerSignUpForm
from ..models import User, Items, Orders
from ..decorators import buyer_required
# Create your views here.

class BuyerSignUpView(CreateView):
    model = User
    form_class = BuyerSignUpForm
    template_name = 'registration/signup_form.html'
    
    success_url = reverse_lazy('buyer:items_list')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'buyer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('buyer:items_list')


@method_decorator([login_required, buyer_required], name='dispatch')
class ItemsListView(ListView):
    model = Items
    ordering = ('name',)
    context_object_name = 'items'
    template_name ='products/buyer/items_home_list.html'

    def get_queryset(self):
        queryset = Items.objects.all()
        return queryset

@method_decorator([login_required, buyer_required], name='dispatch')
class OrdersListView(ListView):
    model = Orders
    ordering = ('name',)
    context_object_name = 'orders'
    template_name ='products/buyer/orders_home_list.html'

    success_url = reverse_lazy('buyer:items_list')
    def get_queryset(self):
        queryset = Orders.objects.filter(owner=self.request.user)
        return queryset

@login_required
@buyer_required
def AddInCart(request, pk):
    item = Items.objects.get(pk=pk)
    order = Orders(owner=request.user, item=item, status=Orders.STATUS[0][0])
    order.save()
    return redirect('buyer:items_list')
