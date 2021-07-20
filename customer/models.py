from django.db import models


class Customer(models.Model):
    company_name = models.CharField(max_length=250)
    budget = models.PositiveIntegerField()
    employment = models.PositiveIntegerField()
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
