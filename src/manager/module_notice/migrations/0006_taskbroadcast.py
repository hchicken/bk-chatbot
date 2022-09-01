# Generated by Django 2.2.16 on 2022-08-31 11:49

import common.models.base
import common.models.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_notice', '0005_auto_20220818_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskBroadcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biz_id', models.CharField(max_length=256, verbose_name='业务ID')),
                ('task_id', models.CharField(max_length=256, verbose_name='任务ID')),
                ('platform', models.CharField(choices=[('JOB', 'JOB'), ('SOPS', '标准运维'), ('DEVOPS', '蓝盾'), ('DEFINE', '自定义')], max_length=32, verbose_name='任务所属平台')),
                ('start_user', models.CharField(max_length=256, verbose_name='开始播报人')),
                ('stop_user', models.CharField(max_length=256, verbose_name='终止播报人')),
                ('start_time', common.models.base.FormatDateTimeField(verbose_name='开始播报时间')),
                ('stop_time', common.models.base.FormatDateTimeField(verbose_name='终止播报时间')),
                ('session_id', models.CharField(max_length=256, verbose_name='触发实时播报的会话ID')),
                ('step_id', models.CharField(max_length=256, verbose_name='任务当前步骤ID')),
                ('step_status', models.CharField(max_length=256, verbose_name='当前步骤状态')),
                ('is_stop', models.BooleanField(default=False, verbose_name='是否停止播报')),
                ('share_group_list', common.models.json.DictCharField(default=[], verbose_name='分享播报用户组列表')),
            ],
            options={
                'verbose_name': '【任务播报】',
                'verbose_name_plural': '【任务播报】',
                'db_table': 'tab_task_broadcast',
            },
        ),
    ]
