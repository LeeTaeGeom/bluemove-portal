# Generated by Django 3.0.6 on 2021-07-05 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applynsubmit', '0006_applymembership_last_saved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applymembership',
            name='failed',
        ),
        migrations.RemoveField(
            model_name='applymembership',
            name='passed',
        ),
        migrations.AddField(
            model_name='applymembership',
            name='pf',
            field=models.CharField(blank=True, choices=[('선발', '선발'), ('미선발', '미선발'), ('미결정', '미결정')], max_length=5, null=True),
        ),
    ]
