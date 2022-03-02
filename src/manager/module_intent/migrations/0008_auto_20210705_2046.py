# Generated by Django 2.2.6 on 2021-07-05 20:46

from django.db import migrations, models
import common.models.base


class Migration(migrations.Migration):

    dependencies = [
        ("module_intent", "0007_auto_20210423_1209"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bot",
            name="created_at",
            field=common.models.base.FormatDateTimeField(auto_now_add=True, null=True, verbose_name="创建时间"),
        ),
        migrations.AlterField(
            model_name="bot",
            name="deleted_at",
            field=common.models.base.FormatDateTimeField(blank=True, null=True, verbose_name="删除时间"),
        ),
        migrations.AlterField(
            model_name="bot",
            name="updated_at",
            field=common.models.base.FormatDateTimeField(blank=True, null=True, verbose_name="更新时间"),
        ),
        migrations.AlterField(
            model_name="executionlog",
            name="created_at",
            field=common.models.base.FormatDateTimeField(auto_now_add=True, null=True, verbose_name="创建时间"),
        ),
        migrations.AlterField(
            model_name="executionlog",
            name="deleted_at",
            field=common.models.base.FormatDateTimeField(blank=True, null=True, verbose_name="删除时间"),
        ),
        migrations.AlterField(
            model_name="executionlog",
            name="platform",
            field=models.IntegerField(default=0, max_length=128, verbose_name="平台类型"),
        ),
        migrations.AlterField(
            model_name="executionlog",
            name="task_id",
            field=models.CharField(default="", max_length=128, verbose_name="任务ID"),
        ),
        migrations.AlterField(
            model_name="executionlog",
            name="updated_at",
            field=common.models.base.FormatDateTimeField(blank=True, null=True, verbose_name="更新时间"),
        ),
        migrations.AlterField(
            model_name="intent",
            name="created_at",
            field=common.models.base.FormatDateTimeField(auto_now_add=True, null=True, verbose_name="创建时间"),
        ),
        migrations.AlterField(
            model_name="intent",
            name="deleted_at",
            field=common.models.base.FormatDateTimeField(blank=True, null=True, verbose_name="删除时间"),
        ),
        migrations.AlterField(
            model_name="intent",
            name="updated_at",
            field=common.models.base.FormatDateTimeField(blank=True, null=True, verbose_name="更新时间"),
        ),
        migrations.AlterField(
            model_name="task",
            name="created_at",
            field=common.models.base.FormatDateTimeField(auto_now_add=True, null=True, verbose_name="创建时间"),
        ),
        migrations.AlterField(
            model_name="task",
            name="deleted_at",
            field=common.models.base.FormatDateTimeField(blank=True, null=True, verbose_name="删除时间"),
        ),
        migrations.AlterField(
            model_name="task",
            name="updated_at",
            field=common.models.base.FormatDateTimeField(blank=True, null=True, verbose_name="更新时间"),
        ),
        migrations.AlterField(
            model_name="utterances",
            name="created_at",
            field=common.models.base.FormatDateTimeField(auto_now_add=True, null=True, verbose_name="创建时间"),
        ),
        migrations.AlterField(
            model_name="utterances",
            name="deleted_at",
            field=common.models.base.FormatDateTimeField(blank=True, null=True, verbose_name="删除时间"),
        ),
        migrations.AlterField(
            model_name="utterances",
            name="updated_at",
            field=common.models.base.FormatDateTimeField(blank=True, null=True, verbose_name="更新时间"),
        ),
    ]