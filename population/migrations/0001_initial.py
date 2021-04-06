# Generated by Django 3.1.7 on 2021-04-05 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dist_name', models.CharField(max_length=50)),
                ('total', models.BigIntegerField()),
                ('males', models.BigIntegerField()),
                ('females', models.BigIntegerField()),
            ],
        ),
    ]
