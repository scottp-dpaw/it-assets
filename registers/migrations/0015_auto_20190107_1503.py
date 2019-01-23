# Generated by Django 2.0.9 on 2019-01-07 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0014_auto_20190104_1157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itsystem',
            old_name='system_type',
            new_name='application_type'
        ),
        migrations.AlterField(
            model_name='changelog',
            name='change_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registers.ChangeRequest'),
        ),
        migrations.AlterField(
            model_name='changerequest',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Draft'), (1, 'Submitted for endorsement'), (2, 'Scheduled for CAB'), (3, 'Ready for implementation'), (4, 'Complete'), (5, 'Rolled back'), (6, 'Cancelled')], db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='itsystem',
            name='seasonality',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Bushfire season'), (2, 'End of financial year'), (3, 'Annual reporting'), (4, 'School holidays'), (5, 'Default')], help_text='Season/period when this system is most important', null=True),
        ),
    ]