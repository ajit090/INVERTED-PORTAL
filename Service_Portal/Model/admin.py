from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Oem,Specification,Dealer,Battery,Client,Complaint,Customerissue,IssueRaisedBy,AdditionalInfo,Resolution,Resolutiontype,Application,Status,Diagnosis,Priority

class BatteryAdmin(admin.ModelAdmin):
    list_display=('serial_no','specification','battery_type','oem','short_cell_description','long_cell_description','bms_specification')
    list_filter = ['serial_no','oem']

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('created_by','assign_by','complaint_id','customer_issue')
    list_filter = ['complaint_id']
 



admin.site.register(Oem)
admin.site.register(Battery,BatteryAdmin)
admin.site.register(Specification)
admin.site.register(Dealer)
admin.site.register(Client)
admin.site.register(Complaint,ComplaintAdmin)
admin.site.register(Application)
admin.site.register(Customerissue)
admin.site.register(IssueRaisedBy)
admin.site.register(AdditionalInfo)
admin.site.register(Resolution)
admin.site.register(Resolutiontype)
admin.site.register(Status)
admin.site.register(Diagnosis)
admin.site.register(Priority)

