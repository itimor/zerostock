# Generated by Django 3.1.5 on 2021-01-31 14:39

from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='标题')),
                ('cover', models.CharField(blank=True, max_length=255, verbose_name='封面')),
                ('slug', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='slug')),
                ('content', mdeditor.fields.MDTextField(default='', verbose_name='正文')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='热度')),
                ('status', models.CharField(choices=[('d', '草稿'), ('p', '已发布'), ('w', '撤销')], default='d', max_length=1, verbose_name='状态')),
                ('is_top', models.BooleanField(default=False, verbose_name='置顶')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(null=True, verbose_name='更新时间')),
                ('publish_time', models.DateTimeField(null=True, verbose_name='发布时间')),
                ('allow_comments', models.BooleanField(default=True, verbose_name='开启评论')),
            ],
            options={
                'verbose_name': '博客文章',
                'verbose_name_plural': '博客文章',
            },
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='名称')),
                ('link', models.URLField(default='', verbose_name='链接')),
                ('cover', models.CharField(blank=True, max_length=255, verbose_name='头像')),
                ('desc', models.TextField(default='未添加描述', verbose_name='描述')),
                ('position', models.SmallIntegerField(default=1, verbose_name='位置')),
                ('active', models.BooleanField(default=True, verbose_name='激活')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('active', models.BooleanField(default=True, verbose_name='激活')),
                ('name', models.CharField(default='佚名', max_length=20, verbose_name='姓名')),
                ('email', models.EmailField(default='pony@qq.com', max_length=20, verbose_name='邮箱')),
                ('content', models.TextField(verbose_name='内容')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.article', verbose_name='博客')),
            ],
            options={
                'verbose_name': '博客评论',
                'verbose_name_plural': '博客评论',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('is_root', models.BooleanField(default=False, verbose_name='是否是一级分类')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='名称')),
                ('slug', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='slug')),
                ('parent', models.ForeignKey(blank=True, default=0, limit_choices_to={'is_root': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myblog.category', verbose_name='父级')),
            ],
            options={
                'verbose_name': '博客类别',
                'verbose_name_plural': '博客类别',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myblog.category', verbose_name='博客类别'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='标签'),
        ),
    ]
