# Generated by Django 4.0.6 on 2022-08-06 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_page', '0004_alter_blog_photo_alter_random_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/blogs/'),
        ),
        migrations.AlterField(
            model_name='random',
            name='photo',
            field=models.ImageField(upload_to='uploads/random/'),
        ),
    ]
