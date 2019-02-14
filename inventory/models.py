from django.db import models
from django.utils import timezone


class Pharmaceutical(models.Model):
    name = models.CharField(max_length=256)
    medicalPrescription = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Pharmaceuticals"


class Medicine(models.Model):
    type = models.ForeignKey(Pharmaceutical, on_delete=models.CASCADE)
    insertDate = models.DateField(auto_now_add=True)
    expirationDate = models.DateField()

    def is_medicine_expired(self):
        if self.expirationDate is not None :
            return timezone.now().date() > self.expirationDate
    is_expired = property(is_medicine_expired)

    class Meta:
        abstract = True
        verbose_name_plural = "Medicines"


class Pill(Medicine):
    def __str__(self):
        return "(ID:" + self.id.__str__() + ") " + self.type.__str__() + " Exp.: " + self.expirationDate.__str__()

    class Meta:
        verbose_name_plural = "Pills"


class Syrup(Medicine):
    openedDate = models.DateField()
    validity = models.IntegerField()

    def __str__(self):
        return "(ID:" + self.id.__str__() + ") " + self.type__str__() + " Exp.: " + self.expirationDate.__str__() + \
               " Opened: " + self.expirationDate.__str__()

    class Meta:
        verbose_name_plural = "Syrups"


