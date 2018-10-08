# Generated by Django 2.0.8 on 2018-09-12 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0005_remove_changeapproval_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changerequest',
            name='implementer',
            field=models.ForeignKey(blank=True, help_text='Request carried out by', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='request_providor', to='organisation.DepartmentUser'),
        ),
    ]
