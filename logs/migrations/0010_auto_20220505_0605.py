# Generated by Django 3.2.13 on 2022-05-05 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0009_user_profile_his_log_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile_his',
            name='new_email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Новый email address'),
        ),
        migrations.AlterField(
            model_name='user_profile_his',
            name='old_email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Старый email address'),
        ),
        migrations.AlterField(
            model_name='user_profile_his',
            name='username',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Никнейм'),
        ),
    ]
