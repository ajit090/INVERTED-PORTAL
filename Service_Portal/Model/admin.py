from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Oem,Specification,Dealer,Battery,Client,Complaint

class BatteryAdmin(admin.ModelAdmin):
    list_display=('serial_no','specification','battery_type','oem','short_cell_description','long_cell_description','bms_specification')
    list_filter = ['serial_no','oem']



admin.site.register(Oem)
admin.site.register(Battery,BatteryAdmin)
admin.site.register(Specification)
admin.site.register(Dealer)
admin.site.register(Client)
admin.site.register(Complaint)

