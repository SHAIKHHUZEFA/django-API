# Generated by Django 3.0.3 on 2020-02-12 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=15)),
                ('bookauthor', models.CharField(max_length=20)),
                ('bookprice', models.IntegerField()),
            ],
        ),
    ]
