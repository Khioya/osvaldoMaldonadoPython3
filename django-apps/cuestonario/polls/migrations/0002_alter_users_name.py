# Generated by Django 4.1.7 on 2023-04-03 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(default='Nombre', max_length=256),
        ),
    ]
