# Generated by Django 2.2.4 on 2022-02-01 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_course'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='Courses',
        ),
    ]
