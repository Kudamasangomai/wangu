# Generated by Django 4.0.4 on 2022-04-13 21:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_lastname', models.CharField(max_length=100)),
                ('contact_email', models.CharField(max_length=100)),
                ('contact_phone', models.CharField(max_length=20)),
                ('contact_address', models.CharField(max_length=100)),
                ('contact_image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
