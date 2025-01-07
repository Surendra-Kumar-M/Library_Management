# Generated by Django 5.1.4 on 2025-01-07 14:48

import datetime
import django.core.validators
import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Book Title')),
                ('author', models.CharField(max_length=50, verbose_name='Author Name')),
                ('genre', models.CharField(choices=[('Fiction', 'Fiction'), ('Non-Fiction', 'Non-Fiction'), ('Sci-Fi', 'Sci-Fi'), ('Biography', 'Biography')], max_length=50)),
                ('publication_year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2025)], verbose_name='Year of Publication')),
                ('available_copies', models.PositiveIntegerField(default=0, verbose_name='Available Copies')),
                ('isbn_number', models.IntegerField(max_length=13, unique=True, verbose_name='ISBN Number')),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Book Rating')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=50, verbose_name='Name')),
                ('mail', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone Number')),
                ('membership_start_date', models.DateField(default=datetime.datetime(2025, 1, 7, 20, 18, 50, 868832))),
                ('membership_type', models.CharField(choices=[('Basic', 'Basic'), ('Premium', 'Premium'), ('Elite', 'Elite')], max_length=20)),
                ('max_books_allowed', models.SmallIntegerField(default=2)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(max_length=50, verbose_name='Staff_Name')),
                ('mail', models.EmailField(max_length=254, verbose_name='Email')),
                ('role', models.CharField(choices=[('Librarian', 'Librarian'), ('Assistant', 'Assistant')], default='Assistant', max_length=15)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone Number')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('issue_date', models.DateField(default=datetime.date(2025, 1, 7))),
                ('return_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Issued', 'Issued'), ('Returned', 'Returned'), ('Overdue', 'Overdue')], default='Issued', max_length=20)),
                ('fine_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='info.book')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='info.member')),
            ],
        ),
    ]
