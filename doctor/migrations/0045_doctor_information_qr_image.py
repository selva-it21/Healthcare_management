# Generated by Django 4.2.4 on 2023-09-22 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0044_appointment_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_information',
            name='qr_image',
            field=models.ImageField(blank=True, default='doctors_qr/usr-default.png', null=True, upload_to='doctors_qr/'),
        ),
    ]
