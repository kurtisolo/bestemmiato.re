# Generated by Django 4.2.2 on 2023-06-28 10:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BestemmiaBacheca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bestemmia_bacheca', models.CharField(max_length=500)),
                ('data_bestemmia', models.DateField(default=datetime.date.today)),
                ('likes_bestemmia', models.IntegerField(default=0)),
            ],
        ),
    ]
