# Generated by Django 3.0.6 on 2021-08-12 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applynsubmit', '0032_auto_20210729_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applymembership',
            name='pf',
            field=models.CharField(blank=True, choices=[('선발', '선발'), ('미결정', '미결정'), ('미선발', '미선발')], default='미결정', max_length=5, null=True),
        ),
    ]