# Generated by Django 4.2.2 on 2023-07-01 10:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bacheca", "0002_alter_bestemmiabacheca_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="bestemmiabacheca",
            name="audio_file_path",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
