from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class States(models.Model):
    name = models.CharField(max_length=128, null=True)

    def __str__(self) :
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=128, null=True)

    def __str__(self) :
        return self.name

class ISO(models.Model):
    name = models.CharField(max_length=4, null=True)

    def __str__(self) :
        return self.name


class Site(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    description = models.CharField(max_length=128)
    justification = models.CharField(max_length=128)
    longitude = models.DecimalField(max_digits=19, decimal_places=10, null=True)
    latitude = models.DecimalField(max_digits=19, decimal_places=10, null=True)
    area_hectares = models.DecimalField(max_digits=19, decimal_places=10, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    states = models.ForeignKey(States, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    iso = models.ForeignKey(ISO, on_delete=models.CASCADE)

    def __str__(self) :
        return "category "+ str(self.category.id) + " <--> states " + str(self.states.id) + " <--> region "+ str(self.region.id) + " <--> iso " + str(self.iso.id)





