# Generated by Django 3.2.6 on 2021-08-20 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_alter_membertask_taskname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membertask',
            name='TaskName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='task.task'),
        ),
    ]
