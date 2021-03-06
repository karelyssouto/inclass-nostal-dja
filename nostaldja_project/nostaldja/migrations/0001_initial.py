# Generated by Django 2.1.5 on 2019-02-12 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Decade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Fads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, default='')),
                ('image_url', models.CharField(max_length=500, default='')),
                ('description', models.TextField()),
                ('decade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fads', to='nostaldja.Decade')),
            ],
        ),
    ]
