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
    status_choices = (
        ("approved", "approved"),
        ("rejected", "rejected"),
        ("pending", "pending"),
    )
    name = models.CharField(max_length=30)
    place=models.ForeignKey(Marketplace,on_delete=models.CASCADE,null=True,related_name='brands')
    code=models.ForeignKey(Zipcode,on_delete=models.CASCADE,null=True)
    image = models.FileField(upload_to='ProductImage', null=True, blank=True)
    status=models.CharField(max_length=30,default='pending',choices=status_choices)
    created_date=models.DateField()
    def __str__(self) -> str:
        return self.name
    class Meta:
        ordering = ['name']


class Feed(models.Model):
    status_choices = (
        ("approved", "approved"),
        ("rejected", "rejected"),
        ("pending", "pending"),
    )
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,null=True,related_name='feed')
    subject=models.CharField(max_length=3000,null=True)
    sprit_category=models.CharField(max_length=50,null=True)
    sprit_subcategory=models.CharField(max_length=50,null=True)
    wine_category=models.CharField(max_length=50,null=True)
    wine_subcategory=models.CharField(max_length=50,null=True)
    beer_category=models.CharField(max_length=50,null=True)
    beer_subcategory=models.CharField(max_length=50,null=True)
    status=models.CharField(max_length=30,default='pending',choices=status_choices)
