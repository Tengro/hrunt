# Generated by Django 3.2.12 on 2022-02-27 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_id', models.BigIntegerField(unique=True, verbose_name='Telegram User ID')),
                ('chat_id', models.BigIntegerField(verbose_name='Telegram Chat ID')),
                ('first_name', models.CharField(max_length=64, verbose_name='Telegram Firstname')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
