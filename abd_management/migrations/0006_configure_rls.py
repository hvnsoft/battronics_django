# Generated by Django 4.0.4 on 2023-09-12 13:02

from django.db import migrations

tenant = "0"


class Migration(migrations.Migration):
    dependencies = [
        ('abd_management', '0005_auto_20230912_1431'),
    ]

    operations = [
        migrations.RunSQL(sql=f"SET abd.active_tenant={tenant}"),
        migrations.RunSQL(sql=f"SET abd.change_owner_battid={None}")
    ]
