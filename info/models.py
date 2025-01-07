from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from phonenumber_field.modelfields import PhoneNumberField
import phonenumbers


# Create your models here.
class Book(models.Model):
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
    isbn_number = models.IntegerField(unique=True, verbose_name='ISBN Number')
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, verbose_name='Book Rating')
    
class Member(models.Model):
    TYPES=[
        ('Basic','Basic'),
        ('Premium','Premium'),
        ('Elite','Elite')
    ]
    member_name=models.CharField(max_length=50, verbose_name="Name")
    mail=models.EmailField(unique=True, verbose_name="Email")
    phone=PhoneNumberField(verbose_name="Phone Number")
    membership_start_date=models.DateField(default=now)
    membership_type=models.CharField(max_length=20,choices=TYPES)
    max_books_allowed = models.SmallIntegerField(default=2)  # Removed condition-based validation
    
    def save(self, *args, **kwargs):
        # Automatically set max_books_allowed based on membership_type
        if self.membership_type == 'Basic':
            self.max_books_allowed = 2
        elif self.membership_type == 'Premium':
            self.max_books_allowed = 5
        elif self.membership_type == 'Elite':
            self.max_books_allowed = 10
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.member_name
    
class Transaction(models.Model):
    STATUS_CHOICES = [
        ('Issued', 'Issued'),
        ('Returned', 'Returned'),
        ('Overdue', 'Overdue'),
    ]

    transaction_id = models.AutoField(primary_key=True)
    member = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='transactions')
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='transactions')
    issue_date = models.DateField(default=now)
    return_date = models.DateField(null=True, blank=True)  # Optional initially
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Issued')
    fine_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, validators=[MinValueValidator(0)])



    def clean(self):
        # Check if the book has available copies
        if self.book.available_copies <= 0:
            raise ValidationError(f"The book '{self.book.title}' is not available for issue.")
        # Validate return_date > issue_date
        if self.return_date and self.return_date <= self.issue_date:
            raise ValidationError("Return date must be greater than issue date.")

    def save(self, *args, **kwargs):
        # Perform validations
        self.clean()

        # Automatically calculate fine for overdue books
        if self.status == 'Overdue' and self.return_date:
            overdue_days = (self.return_date - self.issue_date).days - 15  # Assuming 14-day borrowing period
            self.fine_amount = max(overdue_days * 5, 0)  # $5 per overdue day
        else:
            self.fine_amount = 0.00

        # Deduct available copies if the status is 'Issued'
        if self.status == 'Issued':
            self.book.available_copies -= 1
            self.book.save()

        if self.status == 'Returned':
            self.book.available_copies += 1
            self.book.save()


        super().save(*args, **kwargs)

    def __str__(self):
        return f"Transaction {self.transaction_id} - {Member.member_name}"

class Staff(models.Model):
    STAFF_TYPE=[
        ('Librarian', 'Librarian'),
        ('Assistant','Assistant')
    ]
    staff_name=models.CharField(max_length=50, verbose_name="Staff_Name")
    mail=models.EmailField(unique=True,verbose_name="Email")
    role=models.CharField(max_length=15,choices=STAFF_TYPE,default="Assistant")
    phone=PhoneNumberField(verbose_name="Phone Number")
    
    def __str__(self):
        return self.staff_name
    
