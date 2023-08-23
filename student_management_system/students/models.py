from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    marks = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
