# Generated by Django 2.0.8 on 2018-09-27 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0016_remove_changerequest_standard_change'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changeapproval',
            name='date_approved',
            field=models.DateTimeField(blank=True, help_text='Date change was approved/rejected.', null=True),
        ),
        migrations.AlterField(
            model_name='changerequest',
            name='implementation_docs',
            field=models.FileField(blank=True, null=True, upload_to='uploaded_files/', verbose_name='Implementation Documents'),
        ),
    ]
