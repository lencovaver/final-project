# Generated by Django 4.2.2 on 2023-06-29 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0016_alter_postjob_experience_alter_postjob_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postjob',
            name='category',
            field=models.CharField(blank=True, choices=[('', '---------'), ('AM', 'AM 🛵'), ('A1', 'A1'), ('A2', 'A2'), ('A', 'A 🏍️'), ('B1', 'B1 🚚'), ('B', 'B 🚗'), ('C1', 'C1 🚛'), ('C', 'C'), ('D1', 'D1 🚐'), ('D', 'D 🚌'), ('BE', 'BE '), ('C1E', 'C1E'), ('CE', 'CE'), ('D1E', 'D1E'), ('DE', 'DE'), ('T', 'T 🚜')], default='', max_length=100),
        ),
    ]
