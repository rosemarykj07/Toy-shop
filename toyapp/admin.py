from django.contrib import admin
from . models import Reg_tbl,Products_tbl,cart_tbl
# Register your models here.

admin.site.register(Reg_tbl)
admin.site.register(Products_tbl)
admin.site.register(cart_tbl)
