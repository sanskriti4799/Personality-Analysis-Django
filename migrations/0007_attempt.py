# Generated by Django 2.2 on 2019-09-22 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0006_auto_20190922_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confidence_attempt', models.BooleanField()),
                ('confidence_score', models.IntegerField()),
                ('academics_attempt', models.BooleanField()),
                ('academics_score', models.IntegerField()),
                ('fitness_attempt', models.BooleanField()),
                ('fitness_score', models.IntegerField()),
                ('personality_attempt', models.BooleanField()),
                ('personality_score', models.IntegerField()),
                ('attempter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
