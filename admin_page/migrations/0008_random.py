# Generated by Django 4.0.6 on 2022-07-15 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_page', '0007_rename_date_message_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Random',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='uploads/random/')),
            ],
        ),
    ]
