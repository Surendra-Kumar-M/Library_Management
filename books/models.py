from django.db import models


# Create your models here.
class Books(models.Model):
    BookID = id
    Title = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    Genre = models.CharField(max_length=50,
                             choices=[('Fiction', 'Fiction'), ('Non-Fiction', 'Non-Fiction'), ('Sci-Fi', 'Sci-Fi'),
                                      ('Biography', 'Biography')])
    Publication_Year = models.PositiveIntegerField()
    Available_Copies = models.PositiveIntegerField(default=0)
    ISBN_Number = models.CharField(max_length=13, unique=True)
    Rating = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
