from django.db import models

class Product(models.Model):
    pcode = models.IntegerField(default=0)
    ptitle = models.CharField(max_length=1000)
    category1 = models.CharField(max_length=100)
    category2 = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    kg = models.IntegerField()
    price = models.IntegerField(default=0)
    sprice = models.IntegerField(default=0)
    pcount = models.IntegerField(default=0)
    img1 = models.ImageField(null=True, blank=True, upload_to='product')
    img2 = models.ImageField(null=True, blank=True, upload_to='product')
    img3 = models.ImageField(null=True, blank=True, upload_to='product')
    sdate = models.DateTimeField(auto_now=True)
    mdate = models.DateTimeField(auto_now=True)
    sale = models.CharField(max_length=100)
    ntchk = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.pcode}, {self.ptitle}, {self.price}'