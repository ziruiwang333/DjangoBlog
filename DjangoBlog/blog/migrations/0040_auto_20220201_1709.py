# Generated by Django 2.2.4 on 2022-02-01 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0039_auto_20220201_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydetail',
            name='introduction',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mydetail',
            name='phone2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]