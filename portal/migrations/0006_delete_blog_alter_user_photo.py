# Generated by Django 4.0.6 on 2022-07-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_alter_user_role'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, default='uploads/users/default.png', null=True, upload_to='uploads/users/'),
        ),
    ]
