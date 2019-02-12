from django.db import models


class Pharmaceutical(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField
    medicalPrescription = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Pill(models.Model):
    type = models.ForeignKey(Pharmaceutical, on_delete=models.CASCADE)
    insertDate = models.DateField
    expirationDate = models.DateField

    def __str__(self):
        return self.type
