# Generated by Django 2.2.9 on 2020-04-21 11:13

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0020_union_meeting_notes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="union",
            name="founded",
            field=models.DateField(
                default=datetime.datetime(1970, 1, 1), verbose_name="Stiftet"
            ),
            preserve_default=False,
        ),
    ]