# Generated by Django 4.0.4 on 2022-09-15 07:08

from django.db import migrations, models
import django.utils.timezone
import timescale.fields


class Migration(migrations.Migration):

    dependencies = [
        ('abd_database', '0003_dataset_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadbatch',
            name='is_deleted',
        ),
        migrations.AddField(
            model_name='hdf5file',
            name='error_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hdf5file',
            name='forget',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hdf5file',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hdf5file',
            name='status',
            field=models.CharField(choices=[('INIT', 'Initial'), ('PROCESS', 'Processing'), ('SUCCESS', 'Successful'), ('ERROR', 'Error'), ('UNHANDLED', 'Unhandled')], default='INIT', max_length=24),
        ),
        migrations.AddField(
            model_name='hdf5file',
            name='time',
            field=timescale.fields.TimescaleDateTimeField(default=django.utils.timezone.now, interval='1 day'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aggdata',
            name='cycle_id',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddConstraint(
            model_name='hdf5file',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('status__exact', 'ERROR'), ('error_details__isnull', False)), models.Q(models.Q(('status__exact', 'ERROR'), _negated=True), ('error_details__isnull', True)), _connector='OR'), name='details_only_with_error'),
        ),
        migrations.AddConstraint(
            model_name='hdf5file',
            constraint=models.CheckConstraint(check=models.Q(('forget', False), models.Q(('forget', True), models.Q(('status__exact', 'SUCCESS'), _negated=True)), _connector='OR'), name='can_not_forget_if_successful'),
        ),
    ]
