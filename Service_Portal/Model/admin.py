from django.contrib import admin
from .models import Oem,Specification,Dealer,Battery,Client



admin.site.register(Oem)
admin.site.register(Specification)
admin.site.register(Dealer)
admin.site.register(Client)

