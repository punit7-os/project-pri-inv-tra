# Generated by Django 4.2.3 on 2023-12-21 15:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("appoftra", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="packages",
            new_name="package",
        ),
    ]
