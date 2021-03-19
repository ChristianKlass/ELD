# Generated by Django 3.0.6 on 2020-05-29 08:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('lucky_draw', '0002_auto_20200529_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestant',
            name='table_number',
            field=models.IntegerField(default=28),
        ),
        migrations.AlterField(
            model_name='contestant',
            name='ticket_number',
            field=models.IntegerField(default=7588, unique=True),
        ),
        migrations.AlterField(
            model_name='draw',
            name='number_of_winners',
            field=models.IntegerField(default=15),
        ),
        migrations.AlterField(
            model_name='event',
            name='total_number_of_winners',
            field=models.IntegerField(default=91),
        ),
    ]