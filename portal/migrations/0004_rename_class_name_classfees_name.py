# Generated by Django 4.0.6 on 2022-07-18 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_rename_class_name_class_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classfees',
            old_name='class_name',
            new_name='name',
        ),
    ]