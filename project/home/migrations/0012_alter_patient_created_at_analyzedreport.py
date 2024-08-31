# Generated by Django 5.1 on 2024-08-30 16:43

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_personalassistant_reccomendations_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 8, 30, 16, 43, 19, 126477, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.CreateModel(
            name='AnalyzedReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analysis', models.TextField()),
                ('analyzed_at', models.DateTimeField(auto_now_add=True)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.healthreport')),
            ],
        ),
    ]
