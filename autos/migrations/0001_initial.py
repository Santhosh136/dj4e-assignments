# Generated by Django 3.2.2 on 2021-07-15 09:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a make (e.g. Dodge)', max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Make must be greater than 1 character')])),
            ],
        ),
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Nickname must be greater than 1 character')])),
                ('mileage', models.PositiveIntegerField()),
                ('comments', models.CharField(max_length=300)),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autos.make')),
            ],
        ),
    ]
