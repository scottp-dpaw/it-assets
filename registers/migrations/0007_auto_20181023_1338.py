# Generated by Django 2.0.9 on 2018-10-23 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0006_auto_20181023_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changerequest',
            name='description',
            field=models.TextField(blank=True, help_text='A brief description of what the change is for and why it is being undertaken', null=True),
        ),
    ]
