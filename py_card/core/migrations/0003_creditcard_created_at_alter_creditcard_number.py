# Generated by Django 4.1.7 on 2023-03-22 14:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_creditcard_brand"),
    ]

    operations = [
        migrations.AddField(
            model_name="creditcard",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="creditcard",
            name="number",
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
