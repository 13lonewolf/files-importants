# Generated by Django 2.1 on 2019-03-28 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookies', '0003_auto_20190327_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cookie',
            name='name',
            field=models.CharField(blank=True, default='sem nome', max_length=100, null=True, verbose_name='Nome'),
        ),
    ]
