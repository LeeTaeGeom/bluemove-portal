# Generated by Django 3.0.6 on 2021-07-03 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applynsubmit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applymembership',
            name='failed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='applymembership',
            name='passed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='applymembership',
            name='received',
            field=models.BooleanField(default=False),
        ),
    ]
