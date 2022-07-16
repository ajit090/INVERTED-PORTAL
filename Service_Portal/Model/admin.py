from django.contrib import admin
from .models import Oem,Specification,Dealer,Battery,Client

class BatteryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('serial_no','specification')



admin.site.register(Oem)
admin.site.register(Battery)
admin.site.register(Specification)
admin.site.register(Dealer)
admin.site.register(Client)

