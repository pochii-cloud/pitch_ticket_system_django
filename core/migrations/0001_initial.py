# Generated by Django 4.0.4 on 2022-05-11 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('capacity', models.PositiveBigIntegerField()),
                ('location', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Fields',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slogan', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Teams',
            },
        ),
    ]
