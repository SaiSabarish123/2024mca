from django.contrib import admin

# Register your models here.
from .models import Menu,Category

admin.site.register(Category)
admin.site.register(Menu)
