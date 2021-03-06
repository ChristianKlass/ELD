# Generated by Django 3.0.6 on 2020-05-28 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('total_number_of_winners', models.IntegerField(default=42)),
            ],
        ),
        migrations.CreateModel(
            name='Draw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number_of_winners', models.IntegerField(default=19)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lucky_draw.Event')),
            ],
            options={
                'unique_together': {('event', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Contestant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=70)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.EmailField(default='test@test.com', max_length=254)),
                ('ticket_number', models.IntegerField(default=1513, unique=True)),
                ('table_number', models.IntegerField(default=39)),
                ('other_id', models.CharField(blank=True, max_length=50)),
                ('custom_field', models.CharField(blank=True, max_length=50)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lucky_draw.Event')),
            ],
            options={
                'unique_together': {('ticket_number', 'event')},
            },
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number', models.IntegerField()),
                ('draw', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lucky_draw.Draw')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lucky_draw.Event')),
                ('won_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lucky_draw.Contestant')),
            ],
            options={
                'ordering': ['number'],
                'unique_together': {('number', 'event', 'draw', 'won_by')},
            },
        ),
    ]
