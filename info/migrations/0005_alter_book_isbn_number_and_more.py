# Generated by Django 5.1.4 on 2025-01-07 16:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_alter_member_membership_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn_number',
            field=models.IntegerField(unique=True, verbose_name='ISBN Number'),
        ),
        migrations.AlterField(
            model_name='member',
            name='membership_start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='issue_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
