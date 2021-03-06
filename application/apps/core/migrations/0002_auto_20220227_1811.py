# Generated by Django 3.2.12 on 2022-02-27 18:11

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.CreateModel(
            name='HelpRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_type', models.CharField(choices=[('Інше', 'No Data')], default='Інше', max_length=150)),
                ('therapist_preferred_sex', models.CharField(choices=[('Чоловіча', 'Male'), ('Жіноча', 'Female'), ('Жоден з варіантів (інше)', 'Other'), ('Не має значення', 'No Data')], default='Не має значення', max_length=150)),
                ('therapist_preferred_type', models.CharField(choices=[('Початківець', 'Unexperienced'), ('Спеціаліст', 'Experienced')], default='Початківець', max_length=150)),
                ('closure_status', models.CharField(blank=True, choices=[('Відмова', 'Rejection'), ('Неуспішне закриття', 'Failure'), ('Успішне закриття', 'Success')], max_length=150, null=True)),
                ('is_open', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('status_description', models.TextField(blank=True, null=True, verbose_name='Опис ситуації')),
                ('failure_closure_reason', models.TextField(blank=True, null=True, verbose_name='Спеціаліст - причина закриття заявки')),
                ('therapist_feedback', models.TextField(blank=True, null=True, verbose_name='Спеціаліст - фідбек на заявку')),
            ],
            options={
                'db_table': 'help_request',
            },
        ),
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('therapist_type', models.CharField(choices=[('Початківець', 'Unexperienced'), ('Спеціаліст', 'Experienced'), ('Неверифіковано як спеціаліста', 'Unverified')], default='Неверифіковано як спеціаліста', max_length=150)),
                ('user_sex', models.CharField(choices=[('Чоловіча', 'Male'), ('Жіноча', 'Female'), ('Жоден з варіантів (інше)', 'Other'), ('Не бажаю вказувати', 'No Data')], default='Не бажаю вказувати', max_length=150)),
                ('tg_id', models.BigIntegerField(unique=True, verbose_name='Telegram - User ID')),
                ('chat_id', models.BigIntegerField(verbose_name='Telegram - Chat ID')),
                ('first_name', models.CharField(max_length=64, verbose_name="Telegram - ім'я профілю")),
                ('user_age', models.SmallIntegerField(blank=True, null=True, verbose_name='Вік')),
                ('user_preferred_name', models.CharField(max_length=64, verbose_name='Як звертатися')),
                ('user_contact_data', models.CharField(max_length=64, verbose_name='Контактні дані')),
                ('is_therapist', models.BooleanField(blank=True, null=True, verbose_name='Спеціаліст?')),
                ('is_ready_for_clients', models.BooleanField(blank=True, null=True, verbose_name='Готові до кліентів?')),
                ('therapist_themes', models.TextField(blank=True, null=True, verbose_name='Теми спеціаліста')),
                ('therapist_other_data', models.TextField(blank=True, null=True, verbose_name='Спеціаліст - інше')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='helprequest',
            name='therapist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='therapist_requests', to='core.telegramuser'),
        ),
        migrations.AddField(
            model_name='helprequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='core.telegramuser'),
        ),
    ]
