# Generated by Django 2.2.6 on 2021-07-15 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_intent', '0012_merge_20210712_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project_id',
            field=models.CharField(default='', max_length=128, verbose_name='项目id'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_id',
            field=models.CharField(default='', max_length=128, verbose_name='任务ID'),
        ),
    ]
