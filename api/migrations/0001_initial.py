# Generated by Django 3.2.7 on 2021-10-24 07:54

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=200, verbose_name='Модель')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('image_url', models.ImageField(upload_to='', verbose_name='Превью')),
            ],
            options={
                'db_table': 'cars',
            },
        ),
        migrations.CreateModel(
            name='CarIssue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('icon_url', models.ImageField(upload_to='', verbose_name='Иконка')),
                ('is_critical', models.BooleanField(verbose_name='Критически?')),
            ],
            options={
                'db_table': 'car_issues',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Страна')),
            ],
            options={
                'db_table': 'countries',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='HistoryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Страна')),
                ('color', models.CharField(max_length=6, verbose_name='Цвет HEX')),
            ],
            options={
                'db_table': 'history_types',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='LevelTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Путешествие-Тег',
                'verbose_name_plural': 'Путешествия-Теги',
                'db_table': 'travel_tags',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Локация')),
            ],
            options={
                'db_table': 'locations',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='StepType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Страна')),
                ('color', models.CharField(max_length=6, verbose_name='Цвет HEX')),
            ],
            options={
                'db_table': 'step_types',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Путешествие')),
                ('num_likes', models.PositiveIntegerField(verbose_name='Кол-во лайков')),
                ('path_time', models.PositiveIntegerField(verbose_name='Время в пути')),
                ('distance', models.PositiveIntegerField(verbose_name='Дистанция, км')),
                ('image_url', models.ImageField(upload_to='', verbose_name='Превью')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Путешествие',
                'verbose_name_plural': 'Путешествия',
                'db_table': 'travels',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TravelStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ix_step', models.PositiveSmallIntegerField(verbose_name='Шаг')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('coords', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=2, verbose_name='Координаты')),
            ],
            options={
                'verbose_name': 'Шаг путешествия',
                'verbose_name_plural': 'Шаги путешествия',
                'db_table': 'travel_steps',
            },
        ),
        migrations.CreateModel(
            name='UserCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issues', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveSmallIntegerField(), size=None, verbose_name='Проблемы')),
            ],
            options={
                'db_table': 'user_cars',
            },
        ),
        migrations.CreateModel(
            name='UserCarHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ix_history', models.PositiveSmallIntegerField(verbose_name='Шаг')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('date', models.DateField(verbose_name='Дата')),
            ],
            options={
                'db_table': 'user_car_histories',
            },
        ),
        migrations.CreateModel(
            name='UserInsurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_url', models.FileField(upload_to='', verbose_name='Файл')),
                ('start_date', models.DateField(verbose_name='Время начала')),
                ('end_date', models.DateField(verbose_name='Время окончания')),
            ],
            options={
                'db_table': 'user_insurance',
            },
        ),
        migrations.CreateModel(
            name='UserTravel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField(verbose_name='Время начала')),
                ('end_datetime', models.DateTimeField(null=True, verbose_name='Время окончания')),
                ('max_height', models.PositiveIntegerField(verbose_name='Покоренная высота')),
                ('path_passed', models.PositiveBigIntegerField(verbose_name='Км позади')),
                ('is_finished', models.BooleanField(default=False, verbose_name='Окончено?')),
            ],
            options={
                'verbose_name': 'Пользователь-Путешествие',
                'verbose_name_plural': 'Пользователь-Путешествие',
                'db_table': 'user_travels',
            },
        ),
        migrations.CreateModel(
            name='UserTravelStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_passed', models.BooleanField(default=False, verbose_name='Пройдено?')),
                ('id_step', models.ForeignKey(db_column='id_step', on_delete=django.db.models.deletion.CASCADE, to='api.travelstep', verbose_name='Шаг путешествия')),
            ],
            options={
                'verbose_name': 'Пользователь-Шаг путешествия',
                'verbose_name_plural': 'Пользователь-Шаг путешествия',
                'db_table': 'user_travel_steps',
            },
        ),
    ]