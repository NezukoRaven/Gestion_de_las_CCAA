# Generated by Django 2.0.2 on 2022-07-20 04:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token_app_session', models.CharField(blank=True, default='', max_length=240, null=True)),
                ('first_session', models.CharField(blank=True, default='Si', max_length=240, null=True)),
                ('group', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user__username'],
            },
        ),
    ]
