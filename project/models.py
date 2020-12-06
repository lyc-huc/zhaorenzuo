from datetime import datetime

from django.db import models


class Project(models.Model):
    title = models.CharField("标题", max_length=100, default='', blank=True)
    desc = models.CharField("描述", max_length=1000, default='', blank=True)
    skill = models.CharField("所需技能", max_length=500, default='', blank=True)
    industry = models.CharField("所属行业", max_length=200, default='', blank=True)
    over_time = models.CharField("完成时间", max_length=200, default='', blank=True)
    create_time = models.DateTimeField("创建时间", default=datetime.now)
    progress = models.CharField("完成进度", max_length=200, default='0', blank=True)
    address = models.CharField('工作地址', max_length=100, default='', blank=True)
    money = models.CharField('项目预算', max_length=100, default='0', blank=True)
    is_public = models.BooleanField("是否公开", default=True)
    is_pass = models.BooleanField("是否审核通过", default=False)
