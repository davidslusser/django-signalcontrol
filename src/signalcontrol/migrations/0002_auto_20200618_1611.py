# Generated by Django 2.2.12 on 2020-06-18 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signalcontrol', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signalcontrol',
            name='model_name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='signalcontrol',
            unique_together={('app_name', 'signal_name', 'signal_type')},
        ),
    ]