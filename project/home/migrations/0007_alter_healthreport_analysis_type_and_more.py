# Generated by Django 5.1 on 2024-08-28 04:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_healthreport_alter_patient_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthreport',
            name='analysis_type',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='healthreport',
            name='report_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 8, 28, 4, 51, 33, 604897, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]