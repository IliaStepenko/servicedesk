# Generated by Django 3.0.3 on 2020-02-08 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanager', '0002_auto_20200209_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='data_dir',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
