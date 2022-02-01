# Generated by Django 2.2.4 on 2022-02-01 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_mydetail_introduction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Education')),
            ],
        ),
    ]