# Generated by Django 3.0.6 on 2021-07-05 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applynsubmit', '0008_auto_20210705_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applymembership',
            name='pf',
            field=models.CharField(blank=True, choices=[('미선발', '미선발'), ('선발', '선발')], max_length=5, null=True),
        ),
    ]
