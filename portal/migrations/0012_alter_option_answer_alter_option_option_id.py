# Generated by Django 4.0.4 on 2022-07-24 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0011_option_answer_option_option_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='answer',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='option',
            name='option_id',
            field=models.IntegerField(),
        ),
    ]