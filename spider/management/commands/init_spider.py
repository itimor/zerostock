# -*- coding: utf-8 -*-
# author: itimor

from django.core.management.base import BaseCommand, CommandError
from myblog.models import *
from spider.models import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.create(parent=None, is_root=True, name='爬虫', slug='spider')

        self.stdout.write(self.style.SUCCESS('############ 初始化爬虫信息 ###########'))
        SpiderInfo.objects.create(name='零点财经', code='zcaijing', keyword='', base_url='https://www.zcaijing.com')
        SpiderInfo.objects.create(name='巨潮资讯', code='cninfo', keyword='新能源 汽车', base_url='http://www.cninfo.com.cn')
        self.stdout.write(self.style.SUCCESS('初始化完成'))
