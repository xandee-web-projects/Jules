# Generated by Django 4.0.6 on 2022-07-23 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_test_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
