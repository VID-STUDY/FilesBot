# Generated by Django 3.0 on 2019-12-28 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filebot', '0009_file_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='confirmed',
            field=models.BooleanField(default=True),
        ),
    ]
