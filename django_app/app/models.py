from django.db import models
from django.contrib.auth.models import User


class Category (models.Model):

    name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name


class Expense (models.Model):

    title = models.CharField(max_length=250, null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    data = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
