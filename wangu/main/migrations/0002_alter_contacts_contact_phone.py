# Generated by Django 4.0.4 on 2022-04-13 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='contact_phone',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
