# Generated by Django 4.0.4 on 2022-05-19 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learningoutcome',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название образовательного результата'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Необходимо повторить или изучить'),
        ),
    ]