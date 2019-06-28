# Generated by Django 2.1.9 on 2019-06-20 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0024_auto_20190523_0906'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itsystem',
            old_name='retention_disposal_action',
            new_name='disposal_action',
        ),
        migrations.AddField(
            model_name='itsystem',
            name='custody',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Migrate records and maintain for the life of agency'), (2, 'Retain in agency, migrate records to new database or transfer to SRO when superseded'), (3, 'Destroy datasets when superseded, migrate records and maintain for life of agency'), (4, 'Retain 12 months after data migration and decommission (may retain for reference)')], null=True),
        ),
        migrations.AlterField(
            model_name='itsystem',
            name='defunct_date',
            field=models.DateField(blank=True, help_text='Date on which the IT System first becomes a production (legacy) or decommissioned system', null=True),
        ),
        migrations.AlterField(
            model_name='itsystem',
            name='retention_reference_no',
            field=models.CharField(blank=True, help_text='Retention/disposal reference no. in the current retention and disposal schedule', max_length=256, null=True),
        ),
    ]
