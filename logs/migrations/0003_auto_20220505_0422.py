# Generated by Django 3.2.13 on 2022-05-04 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer_his',
            name='offer',
            field=models.UUIDField(blank=True, verbose_name='ID предложения'),
        ),
        migrations.AlterField(
            model_name='offer_log',
            name='offer',
            field=models.UUIDField(blank=True, verbose_name='ID предложения'),
        ),
        migrations.AlterField(
            model_name='order_his',
            name='order',
            field=models.UUIDField(blank=True, verbose_name='ID заказа'),
        ),
        migrations.AlterField(
            model_name='order_log',
            name='order',
            field=models.UUIDField(blank=True, verbose_name='ID заказа'),
        ),
        migrations.AlterField(
            model_name='user_backup',
            name='user',
            field=models.UUIDField(blank=True, verbose_name='ID пользователя'),
        ),
        migrations.AlterField(
            model_name='user_login_his',
            name='user',
            field=models.UUIDField(blank=True, verbose_name='ID пользователя'),
        ),
        migrations.AlterField(
            model_name='user_profile_his',
            name='user',
            field=models.UUIDField(blank=True, verbose_name='ID пользователя'),
        ),
    ]
