# Generated by Django 4.0.6 on 2022-07-15 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_alter_pendingphoto_photo_alter_pendingphoto_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('staff', 'staff'), ('student', 'student')], default=('student', 'student'), max_length=10),
        ),
    ]