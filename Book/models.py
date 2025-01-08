from django.db import models
from django.contrib.auth.models import User

# Create your models here.

Genrechoice=[
    ('Fiction', 'fiction'),
    ('Nonfiction','Nonfiction'),
    ('History','History'),
    ('Psychology','Psychology')
]
class Review(models.Model):
    Title=models.CharField( max_length=50)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    Author=models.CharField(max_length=50)
    Genre=models.CharField( max_length=100 ,choices=Genrechoice, default='Fiction')

    Description=models.TextField()
    Comments=models.TextField()
    Rating=models.CharField(max_length=100)

    def __str__(self):
        return self.Title
    
class Authentic(models.Model):
    username=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=100)
    email=models.EmailField(max_length=100, unique=True)
    first_name=models.CharField(verbose_name='First Name',max_length=100,default='Alice')
    last_name=models.CharField(verbose_name='Last Name',max_length=100,default='carter')
    



       
