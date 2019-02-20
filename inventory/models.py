from django.db import models
from django.utils import timezone
from datetime import timedelta
from model_utils.managers import InheritanceManager


class Pharmaceutical(models.Model):
    name = models.CharField(max_length=256)
    medicalPrescription = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Pharmaceuticals"


class Medicine(models.Model):
    objects = InheritanceManager()
    type = models.ForeignKey(Pharmaceutical, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    insertDate = models.DateField(auto_now_add=True)
    expirationDate = models.DateField()

    def is_medicine_expired(self):
        if self.expirationDate is not None:
            return timezone.now().date() > self.expirationDate
    is_medicine_expired.boolean = True
    is_expired = property(is_medicine_expired)

    class Meta:
        # This class may not be abstract as we will use it to generate searches
        verbose_name_plural = "Medicines"


class Pill(Medicine):
    def __str__(self):
        return "(ID:" + self.id.__str__() + ") " + self.type.__str__() + " Exp.: " + self.expirationDate.__str__()

    class Meta:
        verbose_name_plural = "Pills"


class Bandage(Medicine):
    openedDate = models.DateField(null=True, blank=True)

    def __str___(self):
        return "(ID:" + self.id.__str__() + ") " + self.type.__str__() + " Exp.: " + self.expirationDate.__str__()

    class Meta:
        verbose_name_plural = "Bandages"


class Syrup(Medicine):
    openedDate = models.DateField(null=True, blank=True)
    validity = models.IntegerField()

    def is_medicine_expired(self):
        # Syrup has a specific  expiration date : either it is expired by its date, or it is opened for too long
        if self.openedDate is not None:
            return (self.openedDate + timedelta(days=self.validity)) < timezone.now().date()
        elif self.expirationDate is not None:
            return timezone.now().date() > self.expirationDate
    is_medicine_expired.boolean = True

    def __str__(self):
        return "(ID:" + self.id.__str__() + ") " + self.type.__str__() + " Exp.: " + self.expirationDate.__str__() + \
               " Opened: " + self.openedDate.__str__()

    class Meta:
        verbose_name_plural = "Syrups"


class Tool(Medicine):
    is_sterile = models.BooleanField(default=False)
    openedDate = models.DateField(null=True, blank=True)

    def is_medicine_expired(self):
        # Tool never expires
        return False
    is_medicine_expired.boolean = True

    def __str___(self):
        return "(ID:" + self.id.__str__() + ") " + self.type.__str__()

    class Meta:
        verbose_name_plural = "Tools"
