# Generated by Django 4.2.4 on 2024-04-29 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_todo"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Todo",
        ),
    ]
