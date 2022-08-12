from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=12)
    content = models.TextField()

    def __str__(self) :
        return self.name

class Challenge(models.Model):
    sno = models.AutoField(primary_key= True)
    title = models.CharField(max_length=255)
    link=models.CharField(max_length=130)
    content=models.TextField()

    def __str__(self):
        return self.title

class Answer(models.Model):
    sno= models.AutoField(primary_key=True)
    Ans=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    ques=models.ForeignKey(Challenge, on_delete=models.CASCADE)
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.Ans[0:50]+ "..." + "by" + " " + self.user.username