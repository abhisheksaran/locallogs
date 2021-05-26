from django.shortcuts import render,redirect
from django.views.generic import TemplateView
# Create your views here.


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

def home(request):
    if request.user.is_authenticated:
        if request.user.is_seller:
            return redirect('seller:product_change_list')
        else:
            return redirect('buyer:product_list')
    return render(request, 'products/home.html')