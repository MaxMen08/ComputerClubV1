# Generated by Django 3.2 on 2021-04-22 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neoclub', '0002_auto_20210422_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hall',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название зала'),
        ),
    ]