# Generated by Django 4.0.6 on 2022-07-15 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_alter_user_pending_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='pending_photo',
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Staff', 'staff'), ('Student', 'student')], default=('Student', 'student'), max_length=10),
        ),
        migrations.CreateModel(
            name='PendingPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='uploads/users/pending/')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]