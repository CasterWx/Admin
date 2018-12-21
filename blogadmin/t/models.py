from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(u'标题', max_length=256)
    author = models.CharField(u'作者', max_length=256)
    localurl = models.CharField(u'链接', max_length=256)
    imgurl = models.CharField(u'图片链接', max_length=256)
    time = models.CharField(u'时间', max_length=256)
    review = models.CharField(u'浏览', max_length=256)
    memage = models.CharField(u'留言量', max_length=256)
    code = models.CharField(u'摘要', max_length=256)
    local = models.CharField(u'标签', max_length=256)
    data = models.TextField(u'内容')


class Comment(models.Model):
    url = models.CharField(u'评论文章',max_length=256)
    imgurl = models.CharField(u'头像链接', max_length=256)
    time = models.CharField(u'评论时间', max_length=256)
    name = models.CharField(u'评论者', max_length=256)
    content = models.CharField(u'留言内容', max_length=256)


class Friend(models.Model):
    name = models.CharField(u'昵称',max_length=256)
    img = models.CharField(u'头像链接', max_length=256)
    url = models.CharField(u'友情链接', max_length=256)


class Log(models.Model):
    time = models.CharField(u'时间', max_length=256)
    title = models.CharField(u'内容', max_length=256)


class Music(models.Model):
    name = models.CharField(u'音乐名', max_length=256)
    artist = models.CharField(u'演唱者', max_length=256)
    lrc = models.CharField(u'歌词', max_length=256)
    theme = models.CharField(u'主题', max_length=256)
    url = models.CharField(u'音乐源', max_length=256)
    cover = models.CharField(u'图片',max_length=256)