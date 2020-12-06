from datetime import datetime

from django.contrib.auth.models import AbstractUser
from project.models import Project
from django.db import models


# 用户资料
class UserProfile(AbstractUser):
    gender_choices = (
        ('male', '男'),
        ('female', '女')
    )
    type_choices = (
        ('receive', '接单用户'),
        ('publish', '发单用户')
    )
    nick_name = models.CharField('昵称', max_length=50, default='')
    birthday = models.DateField('生日', null=True, blank=True)
    type = models.CharField('用户类别', max_length=10, choices=type_choices, default='publish')
    gender = models.CharField('性别', max_length=10, choices=gender_choices, default='female', blank=True)
    address = models.CharField('现地址', max_length=100, default='', blank=True)
    mobile = models.CharField('手机号', max_length=13, null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y%m', default='image/default.png', max_length=100, verbose_name='头像')
    project = models.ForeignKey(Project, on_delete=True, blank=True)  # 关联项目

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


# 接单用户额外资料
class OrderUser(UserProfile):
    type_choices = (
        ('freedom', '自由职业'),
        ('fullwork', '全职')
    )
    id_card = models.CharField("身份证", max_length=18, blank=True)
    real_name = models.CharField("真实姓名", max_length=50, blank=True)
    job_time = models.CharField("工作年限", max_length=30, blank=True)
    introduce = models.CharField("简介", max_length=1000, blank=True)
    skill = models.CharField("擅长技能", max_length=100, blank=True)
    industry = models.CharField("所属行业", max_length=200, blank=True)
    create_time = models.DateTimeField("创建时间", default=datetime.now)
    is_pass = models.BooleanField("是否审核通过", default=False)
    is_delete = models.BooleanField(default=False)
    work_status = models.CharField('性别', max_length=10, choices=type_choices, default='freedom', blank=True)
    role = models.CharField("角色", max_length=32, blank=True)

    class Meta:
        verbose_name = '接单用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


# 项目经验
class ProjectExperience(models.Model):
    title = models.CharField("标题", max_length=100, blank=True)
    desc = models.CharField("描述", max_length=1000, blank=True)
    skill = models.CharField("使用技能", max_length=100, blank=True)
    start_time = models.CharField("项目开始时间", max_length=200, blank=True)
    end_time = models.CharField("项目结束时间", max_length=200, blank=True)
    is_delete = models.BooleanField(default=False)
    user = models.ForeignKey(OrderUser, related_name='pe_user', on_delete=True)


# 工作经验
class WorkExperience(models.Model):
    company = models.CharField("公司", max_length=100)
    job_desc = models.CharField("工作内容描述", max_length=1000, blank=True)
    skill = models.CharField("使用技能", max_length=100, blank=True)
    start_time = models.CharField("工作开始时间", max_length=200, blank=True)
    end_time = models.CharField("工作结束时间", max_length=200, blank=True)
    is_delete = models.BooleanField(default=False)
    user = models.ForeignKey(OrderUser, related_name='we_user', on_delete=True)


# 学习经验
class SchoolExperience(models.Model):
    school = models.CharField("学校", max_length=100, blank=True)
    desc = models.CharField("内容描述", max_length=1000, blank=True)
    start_time = models.CharField("学习开始时间", max_length=200, blank=True)
    end_time = models.CharField("学习结束时间", max_length=200, blank=True)
    is_delete = models.BooleanField(default=False)
    user = models.ForeignKey(OrderUser, related_name='se_user', on_delete=True)
