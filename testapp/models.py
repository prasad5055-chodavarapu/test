from django.db import models

# Create your models here.
class Book(models.Model):
    AuthorName=models.CharField(max_length=10)
    BookName=models.CharField(max_length=20)
    ISBNno=models.IntegerField()
    Rdate=models.DateField()

