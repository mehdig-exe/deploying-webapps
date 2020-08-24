# Generated by Django 3.0.8 on 2020-07-16 19:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200714_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_content',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 16, 19, 24, 44, 50901, tzinfo=utc), verbose_name='date published'),
        ),
    ]