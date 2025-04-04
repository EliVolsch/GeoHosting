# Generated by Django 4.2.15 on 2025-03-14 11:02

from django.db import migrations, models
from geohosting.models.instance import Instance, InstanceStatus

def run(apps, schema_editor):
    Instance.objects.filter(status='Terminating').update(
        status=InstanceStatus.DELETING)
    Instance.objects.filter(status='Terminated').update(
        status=InstanceStatus.DELETED)


class Migration(migrations.Migration):

    dependencies = [
        ('geohosting', '0035_alter_instance_unique_together_instance_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='status',
            field=models.CharField(choices=[('Deploying', 'Deploying'), ('Starting Up', 'Starting Up'), ('Online', 'Online'), ('Offline', 'Offline'), ('Deleting', 'Deleting'), ('Deleted', 'Deleted')], default='Deploying'),
        ),
        migrations.RunPython(run, migrations.RunPython.noop),
    ]
