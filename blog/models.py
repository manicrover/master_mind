from email.policy import default
from django.db import models
from django.forms import CharField

# Create your models here.

class blog (models.Model):
    s_no = models.IntegerField(unique=True, null=False)
    name_of_exam = models.CharField(max_length=100,default="examination")
    age_limit = models.IntegerField(verbose_name="age limit")
    required_subjects = models.CharField(max_length=1000)
    percentage_crietria = models.IntegerField()
    suggested_study_material = models.CharField(max_length=100)
    cut_off = models.IntegerField(max_length=3)
    more_details = models.CharField(max_length=10000)
    official_website = models.URLField()
    registration_link = models.URLField()
    source = models.CharField(max_length=1000,verbose_name="cource of info.")
    pass
