# Generated by Django 5.1.1 on 2024-09-21 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mod5app', '0002_rename_appliances_appliance_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appliance',
            old_name='applianceneedsElectric',
            new_name='applianceNeedsElectric',
        ),
    ]
