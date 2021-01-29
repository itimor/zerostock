# -*- coding: utf-8 -*-
# author: itimor

from django.conf.urls import url

from myblog.views import *
from myblog.feeds import ArticleRssFeed

urlpatterns = [
    url(r'^archive/$', ArichiveView.as_view(), name='archive'),
    url(r'^detail/(?P<blog_slug>\w+).html$', ArticleDetailView.as_view(), name='blog_slug'),
    url(r'^add_comment/$', AddCommentView.as_view(), name='add_comment'),
    url(r'^rss/$', ArticleRssFeed(), name='rss'),
    url(r'^tags/$', TagView.as_view(), name='tags'),
    url(r'^tag/(?P<tag_slug>[\w,-]+)/$', TagDetailView.as_view(), name='tag_slug'),
    url(r'^categorys/$', CategoryView.as_view(), name='categorys'),
    url(r'^category/(?P<category_slug>[\w,-]+)/$', CategoryDetaiView.as_view(), name='category_slug'),
]