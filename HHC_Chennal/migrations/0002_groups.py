# Generated by Django 4.2.13 on 2024-09-10 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HHC_Chennal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=250, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('group_name', models.CharField(max_length=128, unique=True)),
            ],
        ),
    ]
