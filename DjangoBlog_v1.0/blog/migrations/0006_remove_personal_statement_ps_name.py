# Generated by Django 2.2.14 on 2020-08-04 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_personal_statement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal_statement',
            name='ps_name',
        ),
    ]
