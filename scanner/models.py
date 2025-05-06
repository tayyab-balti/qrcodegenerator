from django.db import models

# Create your models here.
class QRCode(models.Model):
    data = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.data} - {self.mobile_number}"
    