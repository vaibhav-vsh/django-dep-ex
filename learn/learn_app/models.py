from django.db import models

# Create your models here.
class Kid(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50,unique=True)
    dob=models.DateField()

    def __str__(self):
        return self.name

class Student(models.Model):
    roll_no=models.ForeignKey(Kid,on_delete=models.CASCADE)
    marks=models.IntegerField()
    
