# Generated by Django 2.1.5 on 2019-02-13 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nostaldja', '0002_auto_20190212_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decade',
            name='start_year',
            field=models.CharField(max_length=5),
        ),
    ]
