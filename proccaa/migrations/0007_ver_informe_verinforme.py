# Generated by Django 2.0.2 on 2022-07-25 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proccaa', '0006_ver_informe'),
    ]

    operations = [
        migrations.AddField(
            model_name='ver_informe',
            name='verinforme',
            field=models.IntegerField(blank=True, null=True, verbose_name='informe_id'),
        ),
    ]
