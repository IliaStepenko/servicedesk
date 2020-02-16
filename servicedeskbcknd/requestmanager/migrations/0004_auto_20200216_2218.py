# Generated by Django 3.0.3 on 2020-02-16 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usermanager', '0004_locationdictionary'),
        ('requestmanager', '0003_auto_20200216_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sdrequest',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='location', to='usermanager.LocationDictionary'),
        ),
        migrations.DeleteModel(
            name='LocationDictionary',
        ),
    ]