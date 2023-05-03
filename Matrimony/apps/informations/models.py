from django.db import models
import uuid
from .untils import *


def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    print("uuid :",uuid.uuid4())
    return '%s.%s' % (uuid.uuid4(), ext)

# class Height(models.Model):
#     feet = models.CharField(choices=Feet,max_length=120)
#     inch = models.CharField(choices=Inch,max_length=120)

#     def __str__(self) -> str:
#         return "{} {}".format(self.feet,self.inch)

# class Physical_Information(models.Model):
#     height = models.ForeignKey(Height,on_delete=models.CASCADE)
#     weight = models.IntegerField()
#     phisical_Status = models.CharField(choices=Physical_Status,max_length=120)
#     body_type = models.CharField(choices=Body_type,max_length=120)
#     complexion = models.CharField(choices=Complexion,max_length=120)
#     food_habit = models.CharField(choices=Food_Habit,max_length=120)


#     def __str__(self) -> str:
#         return "{} {} {} {} {} {}".format(self.height,self.weight,self.phisical_Status,self.body_type,self.complexion,self.food_habit)

class Caste(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class SubCaste(models.Model):
    caste = models.ForeignKey(to=Caste,on_delete=models.CASCADE)
    subcaste = models.CharField(max_length=120)

    def __str__(self):
        return self.subcaste



class BasicInformation(models.Model):
    name = models.CharField(max_length=120)
    gender = models.CharField(choices=Gender,max_length=30)
    date_of_birth = models.DateField()
    birth_time = models.TimeField()
    Mother_Tongue = models.CharField(choices=Mother_Tongue,default="Tamil",max_length=120)
    Marital_Status = models.CharField(choices=Marital_Status, default="Unmarried", max_length=120)
    photo1 = models.ImageField(upload_to=upload_to)
    photo2 = models.ImageField(upload_to=upload_to,blank=True,null=True)
    photo3 = models.ImageField(upload_to=upload_to,blank=True,null=True)
    photo4 = models.ImageField(upload_to=upload_to,blank=True,null=True)
    photo5 = models.ImageField(upload_to=upload_to,blank=True,null=True)
    height = models.CharField(choices=Height,max_length=120)
    weight = models.IntegerField()
    phisical_Status = models.CharField(choices=Physical_Status,max_length=120)
    body_type = models.CharField(choices=Body_type,max_length=120)
    complexion = models.CharField(choices=Complexion,max_length=120)
    food_habit = models.CharField(choices=Food_Habit,max_length=120)
    father_name = models.CharField(max_length=120)
    father_job = models.CharField(max_length=120)
    mother_name = models.CharField(max_length=120)
    mother_job = models.CharField(max_length=120)
    no_of_brother = models.IntegerField()
    brother_married = models.CharField(max_length=120)
    no_of_sister = models.IntegerField()
    sister_married = models.CharField(max_length=120)
    educational_qualification = models.CharField(max_length=120)
    job = models.CharField(max_length=120)
    income_per_month = models.CharField(max_length=120)
    Religious = models.CharField(max_length=120)
    Caste = models.ForeignKey(to=Caste, on_delete=models.CASCADE, max_length=120)
    Sub_Caste = models.ForeignKey(to=SubCaste,on_delete=models.CASCADE,max_length=120)
    Gothram = models.CharField(max_length=120)
    Lagnam= models.CharField(choices=Lagnam,max_length=120)
    Raasi= models.CharField(choices=Raasi,max_length=120)
    Star = models.CharField(choices=Star,max_length=120)
    Dosa = models.CharField(max_length=120)
    Raasi_Image = models.ImageField(upload_to=upload_to)
    Navamsam_Image = models.ImageField(upload_to=upload_to)
    contact_person = models.CharField(max_length=120)
    contact_No = models.IntegerField()
    whatsApp = models.IntegerField()
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    district = models.CharField(max_length=120)
    state = models.CharField(max_length=120)


    class Meta:
        verbose_name = "Basic Information"
        verbose_name_plural = "Basic_Informations"

    def __str__(self):
        return "Name :{} Image:{}".format(self.name,self.photo1)





