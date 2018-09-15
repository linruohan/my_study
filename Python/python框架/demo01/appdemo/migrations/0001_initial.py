# Generated by Django 2.0.1 on 2018-02-10 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mysite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('author', models.CharField(max_length=100)),
                ('num', models.IntegerField(max_length=10)),
            ],
        ),
    ]
