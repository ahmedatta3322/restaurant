# Generated by Django 3.2.9 on 2021-11-13 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20211113_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_admin',
            field=models.BooleanField(verbose_name='admin status'),
        ),
    ]