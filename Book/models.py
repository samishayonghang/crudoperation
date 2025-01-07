from django.db import models

# Create your models here.

Genrechoice=[
    ('Fiction', 'fiction'),
    ('Nonfiction','Nonfiction'),
    ('History','History'),
    ('Psychology','Psychology')
]
class Review(models.Model):
    Title=models.CharField( max_length=50)
    Author=models.CharField(max_length=50)
    Genre=models.CharField( max_length=100 ,choices=Genrechoice, default='Fiction')

    Description=models.TextField()
    Comments=models.TextField()
    Rating=models.CharField(max_length=100)

    def __str__(self):
        return self.Title

       
