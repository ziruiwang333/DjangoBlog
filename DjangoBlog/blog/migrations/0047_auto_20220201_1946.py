# Generated by Django 2.2.4 on 2022-02-01 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0046_remove_education_degree'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='subject',
            new_name='major',
        ),
    ]