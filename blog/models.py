from email.policy import default
from django.db import models
from django.forms import CharField

# Create your models here.

class blog (models.Model):
    s_no = models.IntegerField(unique=True, null=False)
    name_of_exam = models.CharField(max_length=100,default="examination")
    age_limit = models.CharField(max_length=500,default="none")
    required_subjects = models.CharField(max_length=1000)
    percentage_crietria = models.CharField(max_length=1000,default="none")
    suggested_study_material = models.CharField(max_length=10000)
    cut_off = models.CharField(max_length=5000)
    more_details = models.CharField(max_length=10000)
    official_website = models.URLField()
    registration_link = models.URLField()
    source = models.CharField(max_length=1000,verbose_name="cource of info.")
    # urlp = models.CharField(max_length=100,default="/")
    pass
