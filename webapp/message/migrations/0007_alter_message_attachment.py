# Generated by Django 4.2.3 on 2023-08-10 21:47

from django.db import migrations, models
import message.validators


class Migration(migrations.Migration):
    dependencies = [
        ("message", "0006_message_attachment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="attachment",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="attachments/",
                validators=[
                    message.validators.validate_pdf,
                    message.validators.validate_file_size,
                ],
            ),
        ),
    ]
