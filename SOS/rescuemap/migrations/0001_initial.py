# Generated by Django 2.2.6 on 2019-10-30 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Situation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
                ('c_lat', models.FloatField()),
                ('c_lon', models.FloatField()),
                ('radius', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Victim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('number', models.IntegerField()),
                ('number_2', models.IntegerField()),
                ('roof', models.BooleanField(default=False)),
                ('info', models.CharField(max_length=5000)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]