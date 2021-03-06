# Generated by Django 3.1.5 on 2021-02-01 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpiderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='名称')),
                ('code', models.CharField(max_length=20, unique=True, verbose_name='code')),
                ('keyword', models.CharField(blank=True, help_text='多个关键字用空格分开', max_length=200, verbose_name='关键字')),
                ('base_url', models.CharField(max_length=100, unique=True, verbose_name='域名')),
            ],
            options={
                'verbose_name': '爬虫信息',
                'verbose_name_plural': '爬虫信息',
            },
        ),
    ]
