# Generated by Django 4.2 on 2023-05-18 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0003_alter_validate_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='validate',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
