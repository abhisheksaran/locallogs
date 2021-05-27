from django.contrib import admin

# Register your models here.
from .models import User, Items, Orders

admin.site.register(User)
admin.site.register(Items)
admin.site.register(Orders)