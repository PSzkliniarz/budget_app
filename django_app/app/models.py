from django.db import models

class Account (models.Model):

    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title