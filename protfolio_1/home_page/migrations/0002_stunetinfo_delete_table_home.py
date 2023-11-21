# Generated by Django 4.2.7 on 2023-11-21 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='stunetInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids', models.IntegerField()),
                ('Name', models.CharField(max_length=40)),
                ('Roll', models.IntegerField(max_length=6)),
                ('Dep', models.CharField(max_length=3)),
                ('Code', models.IntegerField(max_length=2)),
                ('Commnet', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='table_home',
        ),
    ]
