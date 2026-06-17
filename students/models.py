from django.db import models

class Student(models.Model):
    admission_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    aadhaar = models.CharField(max_length=12)

    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)

    student_class = models.CharField(max_length=10)

    photo = models.ImageField(upload_to='students/', blank=True, null=True)

    fa1 = models.IntegerField(default=0)
    fa2 = models.IntegerField(default=0)
    sa1 = models.IntegerField(default=0)
    fa3 = models.IntegerField(default=0)
    fa4 = models.IntegerField(default=0)
    sa2 = models.IntegerField(default=0)

    def __str__(self):
        return self.name