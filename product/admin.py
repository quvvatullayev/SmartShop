from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Category, Product

# Register your models here.
admin.site.unregister([Group])
admin.site.register([Category, Product])
