# Generated by Django 2.2.4 on 2022-02-01 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_post_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='mydetail',
            name='introduction',
            field=models.TextField(null=True),
        ),
    ]
