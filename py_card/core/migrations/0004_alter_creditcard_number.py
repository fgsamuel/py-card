# Generated by Django 4.1.7 on 2023-03-22 18:39

from django.db import migrations
import encrypted_model_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_creditcard_created_at_alter_creditcard_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="creditcard",
            name="number",
            field=encrypted_model_fields.fields.EncryptedCharField(unique=True),
        ),
    ]
