# Generated by Django 2.1 on 2019-03-27 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cookie',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='cookie',
            name='archive',
            field=models.CharField(max_length=500, verbose_name='Arquivo'),
        ),
    ]
