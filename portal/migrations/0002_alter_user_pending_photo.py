# Generated by Django 4.0.6 on 2022-07-14 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pending_photo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/users/pending/'),
        ),
    ]
