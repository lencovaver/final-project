# Generated by Django 4.2.3 on 2023-07-24 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0035_alter_postjob_diet_alter_postjob_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postjob',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
