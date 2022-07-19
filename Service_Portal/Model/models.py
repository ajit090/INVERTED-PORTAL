from django.db import models
from django.contrib.auth.models import User


class Customerissue(models.Model):
    name = models.CharField(max_length=150)

    class  Meta:  
        verbose_name_plural  =  "CUSTOMER ISSUE"

    def __str__(self):
        return self.name

class IssueRaisedBy(models.Model):
    customer = models.CharField(max_length=150)

    class  Meta:  
        verbose_name_plural  =  "CUSTOMER Raised By"

    def __str__(self):
        return self.customer

class AdditionalInfo(models.Model):
    customer_issue = models.ForeignKey(Customerissue, on_delete=models.CASCADE, related_name='additionalinfos')
    name = models.CharField(max_length=150)

    class  Meta:  
        verbose_name_plural  =  "ADDITIONAL INFO"

    def __str__(self):
        return self.name
    
class Resolutiontype(models.Model):
    resolution_type = models.CharField(max_length=250)

    class  Meta:  
        verbose_name_plural  =  "RESOLUTION TYPE"

    def __str__(self):
        return self.resolution_type

class Status(models.Model):
    status = models.CharField(max_length=100)

    class  Meta:  
        verbose_name_plural  =  "STATUS"

    def __str__(self):
        return self.status
    

class Diagnosis(models.Model):
    diagnosis = models.CharField(max_length=150)

    class  Meta:  
        verbose_name_plural  =  "DIAGNOSIS"

    def __str__(self):
        return self.diagnosis

class Priority(models.Model):
    priority = models.CharField(max_length=100)

    class  Meta:  
        verbose_name_plural  =  "PRIORITY"

    def __str__(self):
        return self.priority

class Resolution(models.Model):
    resolution = models.CharField(max_length=150)

    class  Meta:  
        verbose_name_plural  =  "RESOLUTION"

    def __str__(self):
        return self.resolution

class Oem(models.Model):
    oem = models.CharField(max_length=100)
    
    class  Meta:  
         verbose_name_plural  =  "OEM" 

    def __str__(self):
        return self.oem


class Specification(models.Model):
    specification = models.CharField(max_length=150)

    class  Meta:  
        verbose_name_plural  =  "SPECIFICATION"  

    def __str__(self):
        return self.specification


class Battery(models.Model):
    serial_no = models.CharField(max_length=100)
    specification = models.ForeignKey(Specification, on_delete=models.SET_NULL, null=True)
    battery_type = models.CharField(max_length=50)
    oem =  models.ForeignKey(Oem, on_delete=models.SET_NULL, null=True)
    short_cell_description = models.CharField(max_length=150)
    long_cell_description = models.CharField(max_length=250)
    bms_specification = models.CharField(max_length=100)
    cell_brand = models.CharField(max_length=100)
    matal_case_specification = models.CharField(max_length=100)
    nickel_specification = models.CharField(max_length=100)
    nickel_weight = models.CharField(max_length=50)
    nominal_voltage = models.CharField(max_length=50)
    nominal_capacity = models.CharField(max_length=50)



    class  Meta:  
        verbose_name_plural  =  "BATTERY"  

    def __str__(self):
        return self.serial_no



class Dealer(models.Model):
    dealer_name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    state_ut = models.CharField(max_length=150)

    
    class  Meta:  
        verbose_name_plural  =  "DEALER"  

    def __str__(self):
        return self.dealer_name

class Client(models.Model):
    client_name = models.CharField(max_length=100)
    client_no = models.BigIntegerField()

    class  Meta:  
        verbose_name_plural  =  "CLIENT"  

    def __str__(self):
        return self.client_name

class Complaint(models.Model):
    comments= models.CharField(max_length=100,blank=True)
    complaint_id = models.IntegerField()
    created_by =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True,related_name='Created_by',blank=True)
    assign_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,related_name='Assigned_by',blank=True)
    battery = models.ForeignKey(Battery, on_delete=models.SET_NULL, null=True)
    soft_pack_serial_no = models.CharField(max_length=50,blank=True)
    register_date =  models.DateTimeField()
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    dealer = models.ForeignKey(Dealer, on_delete=models.SET_NULL, null=True)
    issue_raised_by = models.ForeignKey(IssueRaisedBy, on_delete=models.SET_NULL, null=True,blank=True)
    customer_issue = models.ForeignKey(Customerissue, on_delete=models.SET_NULL, null=True,related_name='cissues1',blank=True)
    additional_info =models.ForeignKey(AdditionalInfo, on_delete=models.SET_NULL, null=True,related_name='add2',blank=True)
    resolution_type =  models.ForeignKey(Resolutiontype, on_delete=models.SET_NULL, null=True,blank=True)
    observations = models.CharField(max_length=250,blank=True)
    tracker = models.CharField(max_length=100,blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    pickup_date = models.DateTimeField(null=True,blank=True)
    receipt_date = models.DateTimeField(null=True,blank=True)
    closure_date =  models.DateTimeField(null=True,blank=True)
    remark = models.CharField(max_length=150)
    diagnosis =  models.ForeignKey(Diagnosis, on_delete=models.SET_NULL, null=True)
    resolution =  models.ForeignKey(Resolution, on_delete=models.SET_NULL, null=True)
    additional_comments = models.CharField(max_length=150,blank=True)
    capacity_after_testing = models.CharField(max_length=100,blank=True)
    final_remarks = models.CharField(max_length=100,blank=True)
    remarks_dispatched = models.CharField(max_length=250,blank=True)

    class  Meta:  
        verbose_name_plural  =  "COMPLAINT"  

    def __str__(self):
        return self.comments





