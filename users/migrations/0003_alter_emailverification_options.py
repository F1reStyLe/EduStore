# Generated by Django 3.2.18 on 2023-03-01 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20230228_1000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailverification',
            options={'verbose_name': 'Проверенный Email', 'verbose_name_plural': 'Проверенные Email'},
        ),
    ]