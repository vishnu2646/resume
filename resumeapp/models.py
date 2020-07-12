from django.db import models
from django.urls import reverse
# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    age = models.IntegerField()
    dob  = models.DateField()
    sslc = models.CharField(max_length=100,null=True,blank=True)
    hslc = models.CharField(max_length=100,null=True,blank=True)
    cgpa = models.IntegerField()
    languages = models.CharField(max_length=100,null=True,blank=True)
    program = models.CharField(max_length=100,null=True,blank=True)
    experience = models.CharField(max_length=20,blank=True,null=True)
    achivements = models.TextField()
    skils = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('resume-detail',kwargs = {'pk':self.pk})