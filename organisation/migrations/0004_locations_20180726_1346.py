# Generated by Django 2.0.6 on 2018-07-26 05:46

from django.db import migrations


def copy_location_to_user(apps, schema_editor):
    DepartmentUser = apps.get_model('organisation', 'DepartmentUser')
    for user in DepartmentUser.objects.filter(location__isnull=True, org_unit__isnull=False):
        user.location = user.org_unit.location
        user.save()
    return


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0003_auto_20180726_1343'),
    ]

    operations = [
        migrations.RunPython(copy_location_to_user),
    ]