# Generated by Django 4.2.15 on 2024-11-21 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geohosting', '0024_alter_salesorder_app_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('erpnext_code', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(max_length=256)),
                ('code', models.CharField(blank=True, max_length=256, null=True)),
                ('time_zones', models.TextField(blank=True, null=True)),
                ('country_name', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'verbose_name_plural': 'Countries',
                'ordering': ('name',),
            },
        ),
        migrations.RemoveField(
            model_name='userbillinginformation',
            name='country',
        ),
        migrations.AddField(
            model_name='userbillinginformation',
            name='erpnext_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
