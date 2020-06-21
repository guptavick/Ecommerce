from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length = 50)
    category = models.CharField(max_length = 50, default ='')
    sub_category = models.CharField(max_length = 50, default ='')
    product_description = models.CharField(max_length = 500)
    price = models.IntegerField(default =0)
    pub_date = models.DateField()
    image = models.ImageField(upload_to = 'crazysite/images', default = "")


    def __str__(self):
        return self.product_name