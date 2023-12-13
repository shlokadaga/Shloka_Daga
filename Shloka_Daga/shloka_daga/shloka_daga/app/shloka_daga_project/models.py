from django.db import models

class Contacts(models.Model):
    contact_email = models.CharField(max_length = 100)
    contact_name = models.CharField(max_length = 100)
    created_time = models.CharField(max_length=100)
    contact_notes = models.CharField(max_length = 100)
    

    def __str__(self):
        return self.contact_name