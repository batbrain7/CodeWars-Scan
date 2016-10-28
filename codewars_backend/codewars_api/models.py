from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Main_Details(models.Model):

    Barcode = models.IntegerField()
    Name = models.CharField(max_length=25)
    Roll_No = models.CharField(max_length=20)

    def __int__(self):
        return self.Barcode

class Personal_Details(models.Model):

    Barcode = models.IntegerField(unique=True)
    Name = models.CharField(max_length=25)
    Mothers_Name = models.CharField(max_length=25)
    Fathers_Name = models.CharField(max_length=25)
    Address = models.TextField()
    Contact_No = models.IntegerField()
    Email = models.CharField(max_length=50)

    def __int__(self):
            return self.Barcode


class Academic_Details(models.Model):

    Barcode = models.IntegerField()
    Branch = models.CharField(max_length=50)
    Year = models.CharField(max_length=10)
    Sem = models.CharField(max_length=10)
    Average_CGPA = models.FloatField()

    def __int__(self):
        return self.Barcode

class Semester_1(models.Model):

    Barcode = models.IntegerField()
    Maths_1 = models.CharField(max_length=3)
    Physics_1 = models.CharField(max_length=3)
    Basic_Electrical = models.CharField(max_length=3)
    Prog_Fundamentals = models.CharField(max_length=3)
    Engg_Drawing = models.CharField(max_length=3)
    Environment = models.CharField(max_length=3)
    Total_CGPA = models.FloatField()

    def __int__(self):
        return self.Barcode

class Semester_2(models.Model):

    Barcode = models.IntegerField()
    Maths_2 = models.CharField(max_length=3)
    Physics_2 = models.CharField(max_length=3)
    Chemistry = models.CharField(max_length=3)
    Basic_Mechanical = models.CharField(max_length=3)
    Workshop_Practice = models.CharField(max_length=3)
    English= models.CharField(max_length=3)
    Total_CGPA = models.FloatField()

    def __int__(self):
        return self.Barcode

class Library(models.Model):

    Barcode = models.IntegerField()
    Books_Isued = models.TextField()
    Fine_Due = models.FloatField()

    def __int__(self):
        return self.Barcode
