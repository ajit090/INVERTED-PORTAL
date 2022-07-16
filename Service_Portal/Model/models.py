from django.db import models

class Oem(models.Model):
    oem = models.CharField(max_length=100)

    
    class  Meta:  
         verbose_name_plural  =  "OEM1" 

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


    


