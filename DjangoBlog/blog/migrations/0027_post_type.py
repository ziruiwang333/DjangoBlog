# Generated by Django 2.2.4 on 2022-02-01 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20200818_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
    ]