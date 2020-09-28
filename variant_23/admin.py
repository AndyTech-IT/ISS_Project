from django.contrib import admin

from .models import Salespeople, Customers, Orders

admin.site.register(Salespeople)
admin.site.register(Customers)
admin.site.register(Orders)