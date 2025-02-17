# Generated by Django 4.2.2 on 2024-11-19 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, help_text='Опишите место, отвечая на вопрос "где?"', max_length=50, null=True, verbose_name='Место')),
                ('time_when', models.DateTimeField(blank=True, help_text='Опишите время, отвечая на вопрос "когда?"', null=True, verbose_name='Время')),
                ('action', models.CharField(blank=True, help_text='Опишите действие, отвечая на вопрос "что буду делать?"', max_length=50, null=True, verbose_name='Действие')),
                ('is_pleasant', models.BooleanField(blank=True, null=True, verbose_name='Признак приятной привычки')),
                ('regularity', models.PositiveSmallIntegerField(default=1, null=True, verbose_name='Периодичность(1 раз в __ дней)')),
                ('reward', models.CharField(blank=True, help_text='Укажите вознаграждение(не указывать, если указали связанную привычку)', max_length=50, null=True, verbose_name='Вознаграждение')),
                ('time_to_complete', models.IntegerField(blank=True, help_text='Укажите количество секунд на выполнение', null=True, verbose_name='Время на выполнение')),
                ('is_public', models.BooleanField(blank=True, null=True, verbose_name='Признак публичности')),
                ('related_habit', models.ForeignKey(blank=True, help_text='Укажите связанную привычку(не указывать, если указали вознаграждение)', null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit', verbose_name='Связанная привычка')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
                'db_table': 'habit',
            },
        ),
    ]
