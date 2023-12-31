# Generated by Django 4.2.2 on 2023-07-09 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_user_language'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterField(
            model_name='city',
            name='name_city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[('ENG', '🇬🇧 angličtina'), ('CHF', '🇨🇭 švýcarská němčina'), ('DEU', '🇩🇪 němčina'), ('FRA', '🇫🇷 francouzština'), ('ITA', '🇮🇹 italština')], max_length=30, null=True),
        ),
    ]
