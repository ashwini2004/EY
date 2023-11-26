# Generated by Django 4.2.7 on 2023-11-26 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=10)),
                ('past_medical_history', models.TextField()),
                ('symptom_days', models.IntegerField()),
                ('symptoms', models.TextField()),
            ],
        ),
    ]
