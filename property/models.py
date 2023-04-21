from django.db import models


class PropertyType(models.Model):
    property_type = models.CharField(max_length=50)

    def __str__(self):
        return self.property_type

class Neibhorhood(models.Model):
    # property_Name = models.ForeignKey(Property,on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length=50)
 
    def __str__(self):
        return self.name

class PriceRange(models.Model):
    price_range = models.CharField(max_length=50)

    def __str__(self):
        return self.price_range

class Property(models.Model):
    price_range = models.ForeignKey(PriceRange,on_delete=models.CASCADE)
    property_type = models.ForeignKey(PropertyType,on_delete=models.CASCADE)
    neighbhorhood = models.ForeignKey(Neibhorhood,on_delete=models.CASCADE)
    featured = models.BooleanField(default=True)

class PropertyDetails(models.Model):
    propert = models.ForeignKey(Property,on_delete=models.CASCADE)
    property_status = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50)
    city  = models.CharField(max_length=50)
    state  = models.CharField(max_length=50)
    zip_code  = models.CharField(max_length=50)
    price  = models.DecimalField(max_digits=10, decimal_places=5)
    description = models.CharField(max_length=50)
    bedroom = models.IntegerField()
    number_car_garage= models.IntegerField()
    fire_place = models.BooleanField(default=True)
    year_built = models.IntegerField()
    build_up_size  = models.IntegerField()
    lot_size = models.IntegerField()
    property_photo1 = models.ImageField(upload_to ='uploads/% Y/% m/% d/') # pip install Pillow
    property_photo2 = models.ImageField(upload_to ='uploads/% Y/% m/% d/') # pip install Pillow
    property_photo3 = models.ImageField(upload_to ='uploads/% Y/% m/% d/') # pip install Pillow
    property_photo4 = models.ImageField(upload_to ='uploads/% Y/% m/% d/') # pip install Pillow



class Searches(models.Model):
    price_range = models.ForeignKey(PriceRange,on_delete=models.CASCADE)
    property_type = models.ForeignKey(PropertyType,on_delete=models.CASCADE)
    neighbhorhood = models.ForeignKey(Neibhorhood,on_delete=models.CASCADE)
    date_searched = models.DateTimeField(auto_now_add=True, null=True, blank=True)

