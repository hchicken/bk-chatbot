# Generated by Django 2.2.16 on 2022-10-31 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_intent', '0005_intenttag'),
    ]

    operations = [
        migrations.AddField(
            model_name='intent',
            name='tag_name',
            field=models.CharField(default='', max_length=128, verbose_name='标签分类'),
        ),
    ]
