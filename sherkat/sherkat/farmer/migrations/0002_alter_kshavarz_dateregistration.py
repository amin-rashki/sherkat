# Generated by Django 4.1.1 on 2022-12-09 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kshavarz',
            name='dateRegistration',
            field=models.DateTimeField(null=True),
        ),
    ]
