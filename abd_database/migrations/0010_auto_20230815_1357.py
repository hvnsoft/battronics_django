# Generated by Django 4.0.4 on 2023-08-15 13:57

from django.db import migrations


def create_dataset_groups(apps, schema_editor):
    Dataset = apps.get_model('abd_database', 'Dataset')
    Group = apps.get_model('auth', 'Group')
    for dataset in Dataset.objects.exclude(pk=1):
        group = Group.objects.create(name=f'dataset_{dataset.pk}')
        group.save()


class Migration(migrations.Migration):
    dependencies = [
        ('abd_database', '0009_dataset_private_alter_dataset_owner'),
    ]

    operations = [
        migrations.RunPython(create_dataset_groups)
    ]
