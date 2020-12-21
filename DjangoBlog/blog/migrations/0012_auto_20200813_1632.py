# Generated by Django 2.2.14 on 2020-08-13 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200813_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='photos',
            name='album_name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Gallery'),
        ),
    ]