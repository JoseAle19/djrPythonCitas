# Generated by Django 4.1.3 on 2022-11-06 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientAppointmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namePatient', models.CharField(max_length=100)),
                ('lastNamePatient', models.CharField(max_length=100)),
                ('emailPatient', models.EmailField(max_length=100)),
                ('phonePatient', models.CharField(max_length=10)),
                ('descriptionPatient', models.TextField()),
                ('dateAppointment', models.DateField()),
                ('appointmentTime', models.TimeField()),
                ('statustAppointment', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='UsersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('lastname', models.CharField(max_length=100)),
                ('rol', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]