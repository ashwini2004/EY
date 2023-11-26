# Generated by Django 4.2.7 on 2023-11-26 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=10)),
                ('past_medical_history', models.TextField()),
                ('symptom_days', models.IntegerField()),
                ('symptoms', models.TextField()),
                ('output_field_1', models.CharField(max_length=255)),
                ('output_field_2', models.CharField(max_length=255)),
                ('feedback_text', models.TextField()),
            ],
        ),
    ]