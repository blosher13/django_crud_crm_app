from django.db import models

class Record(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=256)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    province = models.CharField(max_length=256)
    country = models.CharField(max_length=256)

    # for each record/object, show the first name and last name for that record in DJANGO admin
    def __str__(self):
        
        return self.first_name + "   " + self.last_name
