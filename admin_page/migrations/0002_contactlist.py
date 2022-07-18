# Generated by Django 4.0.6 on 2022-07-18 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=12)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=7)),
                ('email', models.CharField(max_length=50)),
                ('whatsapp', models.CharField(max_length=12)),
            ],
        ),
    ]
