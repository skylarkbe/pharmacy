from django.db import models


class Pharmaceutical(models.Model):
    name = models.CharField(max_length=256)
    medicalPrescription = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    type = models.ForeignKey(Pharmaceutical, on_delete=models.CASCADE)
    insertDate = models.DateField(auto_now_add=True)
    expirationDate = models.DateField(auto_now_add=True)


class Pill(Medicine):
    def __str__(self):
        return "(ID:" + self.id.__str__() + ") " + self.type.__str__() + " Exp.: " + self.expirationDate.__str__()


class Syrup(Medicine):
    openedDate = models.DateField()
    validity = models.IntegerField()

    def __str__(self):
        return "(ID:" + self.id.__str__() + ") " + self.type__str__() + " Exp.: " + self.expirationDate.__str__() + \
               " Opened: " + self.expirationDate.__str__()
