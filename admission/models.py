from django.db import models
from classroom import models as clsModels
import uuid
# Create your models here.
class Admission(models.Model):
    uuid = uuid.uuid4() 
    student_name = models.CharField(max_length=30)
    class_name = models.ForeignKey(clsModels.Grade, on_delete=models.CASCADE)
    guardian_name = models.CharField(max_length=30)
    student_age = models.IntegerField()
    student_dob = models.DateField()
    student_address = models.CharField(max_length=100)
    student_contact = models.CharField(max_length=10)
    gender = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    student_gender = models.CharField(max_length=10,choices=gender)
    student_email = models.EmailField(max_length=100)
    date_of_admission = models.DateField(auto_now_add=True, blank=True)
    student_photo = models.ImageField()
    student_roll = models.CharField(max_length=10)
    promo_code = models.CharField(blank=True, max_length=30)

    def save(self, *args, **kwargs):
        self.promo_code = str(self.student_name) +  str(self.uuid) 
        super().save(*args, **kwargs)

    

    def __str__(self):
        return str(self.student_name) + " " + str(self.student_roll)




