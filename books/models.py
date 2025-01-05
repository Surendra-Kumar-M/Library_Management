from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

# Create your models here.
class Books(models.Model):
    GENRE_CHOICES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Biography', 'Biography'),
    ]
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    
    title = models.CharField(max_length=50, verbose_name='Book Title')
    author = models.CharField(max_length=50, verbose_name='Author Name')
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    publication_year = models.PositiveIntegerField(
        validators=[MinValueValidator(1900),MaxValueValidator(datetime.datetime.now().year)],
        verbose_name='Year of Publication'
    )
    available_copies = models.PositiveIntegerField(default=0, verbose_name='Available Copies')
    isbn_number = models.CharField(max_length=13, unique=True, verbose_name='ISBN Number')
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, verbose_name='Book Rating')
    
    
