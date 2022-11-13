from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User
import uuid
from django.utils import timezone
from datetime import timedelta
from django.contrib.contenttypes.fields import GenericRelation

categotry = (
    ('Journal','Journal'),
    ('Book Chapters','Book Chapters'),
    ('Books','Books'),
    ('International Reports','International Reports'),
    ('Conference','Conference'),
    

)

reasearchCategory = (
    ('Invited Talks','Invited Talks'),
    ('Editorial Boards','Editorial Boards'),
    ('Conference Presentation','Conference Presentation'),
)
TEAM_MEMBER_TYPE = (
    ('TEAM','TEAM'),
('ALUMINI','ALUMINI')

)

# class Team(models.Model):
#     id = models.AutoField(primary_key=True)
#     name=models.CharField(max_length=250, null=True,blank=True)
#     photo = models.FileField(null=True, blank=True)
#     category = models.CharField(max_length=60, choices=team_memberCategory ,default='Team')
#     def __str__(self):
#         return self.name
    
class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=250, null=True,blank=True)
    photo = models.FileField(null=True, blank=True)
    category = models.CharField(max_length=120, choices= TEAM_MEMBER_TYPE,default='Team')
    def __str__(self):
        return self.name
    
class Publication(models.Model):
    id = models.AutoField(primary_key=True)
    info =models.TextField()
    category = models.CharField(max_length=60, choices=categotry ,default='Journal')

    date = models.DateField(null=True)

    def __str__(self):
        return self.category +" - "+self.info
    



class IpModel(models.Model):
    ip=models.CharField(max_length=100)

    def __str__(self):
        return self.ip

class Contact_form(models.Model):
    name=models.CharField(max_length=250, null=True,blank=True)
    email=models.EmailField(max_length=3000)
    subject=models.CharField(max_length=3000)
    affilation=models.CharField(max_length=3000)
    message=models.TextField()

    def __str__(self):
        return self.name + " - " + self.email

class Award(models.Model):
    image=models.FileField(null=True, blank=True)
    title=models.CharField(max_length=3000,null=True, blank=True)
    url=models.CharField(max_length=3000,null=True, blank=True)
    def __str__(self):
        return self.title


class Media(models.Model):
    image=models.FileField(null=True, blank=True)
    title=models.CharField(max_length=3000,null=True, blank=True)
    description=models.CharField(max_length=3000,null=True, blank=True)
    url=models.CharField(max_length=3000,null=True, blank=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    info =models.TextField()
    date = models.DateField(null=True)

    def __str__(self):
        return self.info 


class Reasearch(models.Model):
    id = models.AutoField(primary_key=True)
    info =models.TextField()
    category = models.CharField(max_length=60, choices=reasearchCategory ,default='Invited Talks')

    date = models.DateField(null=True)

    def __str__(self):
        return self.category +" - "+self.info


class Map_Location(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=600)
    lat=models.CharField(max_length=60)
    lng=models.CharField(max_length=60)


    def __str__(self):
        return self.title+" : "+self.lat +" - "+self.lng


class Gallery_Image(models.Model):
    id = models.AutoField(primary_key=True)
    photo = models.FileField(null=True, blank=True)
    about =models.TextField(null=True,blank=True)
    def __str__(self):
        return str(self.about).capitalize()

class Collaboration(models.Model):
    id = models.AutoField(primary_key=True)
    photo = models.FileField(null=True, blank=True)
    name =models.TextField(null=True,blank=True)
    
    university =models.TextField(null=True,blank=True)
    country =models.TextField(null=True,blank=True)
    
    def __str__(self):
        return str(self.name).capitalize()