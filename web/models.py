from django.db import models
# Create your models here.


class Marketplace(models.Model):
    name = models.CharField(max_length=30)
    logo = models.FileField(upload_to='MarketplaceImage', null=True, blank=True)
    def __str__(self):
        return self.name

class Zipcode(models.Model):
    zipcode = models.CharField(max_length=30)
    def __str__(self):
        return self.zipcode

class Brand(models.Model):
    name = models.CharField(max_length=30)
    place=models.ForeignKey(Marketplace,on_delete=models.CASCADE,null=True)
    code=models.ForeignKey(Zipcode,on_delete=models.CASCADE,null=True)
    image = models.FileField(upload_to='ProductImage', null=True, blank=True)
    status=models.CharField(max_length=30,default='On Going')
    created_date=models.DateField()
    def __str__(self):
        return self.name
