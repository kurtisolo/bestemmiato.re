# Generated by Django 4.2.2 on 2023-07-18 12:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("bacheca", "0004_bestemmiabacheca_autore"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bestemmiabacheca",
            name="likes_bestemmia",
        ),
    ]
