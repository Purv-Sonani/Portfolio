# Generated by Django 3.0.3 on 2025-03-18 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20250314_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
