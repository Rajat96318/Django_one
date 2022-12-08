from django.db import models

# Create your models here.
# models vo ha ijo database ko define karti hai

class Contact(models.Model):  # contact ek table hai hamare DB ka, (name, email, phone etc are columns)
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name + " " + self.email
    

