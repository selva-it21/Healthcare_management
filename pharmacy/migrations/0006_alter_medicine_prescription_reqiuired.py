# Generated by Django 4.0.6 on 2022-09-05 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0005_merge_20220905_2240'),

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='Prescription_reqiuired',
            field=models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=200, null=True),
        ),
    ]
