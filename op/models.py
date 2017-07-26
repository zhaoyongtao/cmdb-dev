#coding=utf-8
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from account.models import *



# 环境字典
class Environ(models.Model):
    env_name = models.CharField(verbose_name='环境名',max_length=128)
    description = models.CharField(verbose_name='描述',max_length=256,blank=True)

    def __str__(self):
        return self.env_name


# 操作系统字典
class Os(models.Model):
    os_name = models.CharField(verbose_name='操作系统',max_length=128)
    description = models.CharField(verbose_name='描述',max_length=256,blank=True)

    def __str__(self):
        return self.os_name


# 项目
class Project(models.Model):
    authstat_choices = (
        (0, '待审批'),
        (1, '通过'),
        (2, '未通过'),
    )

    auth_status = models.IntegerField(verbose_name='审批状态', choices=authstat_choices, default=0)
    unit = models.CharField(verbose_name='项目ID', max_length=128)
    project_name = models.CharField(verbose_name='项目名', max_length=128)
    manager = models.ForeignKey(User, related_name='user_manager', verbose_name='项目经理')
    architect = models.ForeignKey(User, related_name='user_architect', verbose_name='架构师')
    developer = models.ForeignKey(User, related_name='user_developer', verbose_name='开发')
    owner = models.ForeignKey(User, related_name='user_projowner', verbose_name='申请人')
    superviser = models.ForeignKey(User, related_name='user_psuperviser', verbose_name='审批人', null=True ,blank=True)
    git = models.CharField(blank=True, verbose_name='GIT仓库', max_length=512)
    cdate = models.DateTimeField(verbose_name='申请时间', auto_now_add=True)
    remark = models.CharField(verbose_name='备注', max_length=256, blank=True)

    def __str__(self):
        return self.unit


# 资源
class Resource(models.Model):
    status_choices = (
        (0, '待审批'),
        (1, '通过'),
        (2, '未通过'),
    )

    cpu_choices = (
        (2, '2核'),
        (4, '4核'),
        (8, '8核'),
        (16, '16核'),
        (32, '32核'),
        (64, '64核'),
    )

    mem_choices = (
        (2, '2G'),
        (4, '4G'),
        (8, '8G'),
        (16, '16G'),
        (32, '32G'),
        (64, '64G'),
        (128, '128G'),
    )

    disk_choices = (
        (200, '200G'),
        (500, '500G'),
        (1000, '1T'),
        (2000, '2T'),
        (4000, '4T'),
        (8000, '8T'),
        (16000, '16T'),
    )

    number_choices = (
        (1, '1台'),
        (2, '2台'),
        (3, '3台'),
        (4, '4台'),
        (5, '5台'),
        (6, '7台'),
        (8, '8台'),
        (9, '9台'),
        (10, '10台'),
    )

    auth_status = models.IntegerField(verbose_name='审批状态', choices=status_choices, default=0)
    project = models.ForeignKey(Project, verbose_name='所属项目')
    environ = models.ForeignKey(Environ, verbose_name='所属环境')
    purpose = models.CharField(verbose_name='用途', max_length=128, blank=True, null=True)
    cpu = models.IntegerField(verbose_name='CPU', choices=cpu_choices,default=2)
    mem = models.IntegerField(verbose_name='内存', choices=mem_choices,default=2)
    disk = models.IntegerField(verbose_name='磁盘', choices=disk_choices,default=200)
    os = models.ForeignKey(Os, verbose_name='操作系统')
    number = models.IntegerField(verbose_name='申请台数', choices=number_choices)
    apply_user = models.ForeignKey(User, related_name='user_applyer', verbose_name='申请人')
    superviser = models.ForeignKey(User, related_name='user_rsuperviser', verbose_name='审核人', blank=True, null=True)
    cdate = models.DateTimeField(verbose_name='申请时间', auto_now_add=True)

    def __str__(self):
        return self.project


# 物理机
class Server(models.Model):
    state_choices = (
        (0, '空闲'),
        (1, '使用中'),
        (2, '已初始化'),
        (3, '已下线'),
        (4, '已回收'),
    )
    
    user_choices = (
        (0, 'root'),
        (1, 'developer'),
        (2, 'test'),
    )
    
    port_choices = (
        (0,22),
        (1,21312),
        (2,21212),
        (3,53977),
    )

    cpu_choices = (
        (2, '2核'),
        (4, '4核'),
        (8, '8核'),
        (16, '16核'),
        (32, '32核'),
        (64, '64核'),
    )

    mem_choices = (
        (2, '2G'),
        (4, '4G'),
        (8, '8G'),
        (16, '16G'),
        (32, '32G'),
        (64, '64G'),
        (128, '128G'),
    )

    disk_choices = (
        (200, '200G'),
        (500, '500G'),
        (1000, '1T'),
        (2000, '2T'),
        (4000, '4T'),
        (8000, '8T'),
        (16000, '16T'),
    )

    ip = models.GenericIPAddressField(verbose_name='服务器IP')
    environ = models.ForeignKey(Environ, verbose_name='所属环境')
    project = models.ForeignKey(Project, verbose_name='所属项目')
    state = models.IntegerField(verbose_name='状态',choices=state_choices,default=0)
    os = models.ForeignKey(Os,verbose_name='操作系统')
    cpu = models.IntegerField(verbose_name='CPU', choices=cpu_choices,default=2)
    mem = models.IntegerField(verbose_name='内存', choices=mem_choices,default=2)
    disk = models.IntegerField(verbose_name='磁盘', choices=disk_choices,default=200)
    user = models.IntegerField(verbose_name='管理帐号',choices=user_choices,default=0)
    port = models.IntegerField(verbose_name='管理端口',choices=port_choices,default=0)
    remark = models.CharField(verbose_name='备注',max_length=256,blank=True)
    cdate = models.DateTimeField(verbose_name='申请时间',auto_now_add=True)
    
    
    def __str__(self):
        return self.ip


# 虚拟机
class Vhost(models.Model):
    state_choices = (
        (0, '空闲'),
        (1, '使用中'),
        (2, '已初始化'),
        (3, '已下线'),
        (4, '已回收'),
    )

    user_choices = (
        (0, 'root'),
        (1, 'developer'),
        (2, 'test'),
    )

    port_choices = (
        (0,22),
        (1,21312),
        (2,21212),
        (3,53977),
    )

    cpu_choices = (
        (2, '2核'),
        (4, '4核'),
        (8, '8核'),
        (16, '16核'),
        (32, '32核'),
        (64, '64核'),
    )

    mem_choices = (
        (2, '2G'),
        (4, '4G'),
        (8, '8G'),
        (16, '16G'),
        (32, '32G'),
        (64, '64G'),
        (128, '128G'),
    )

    disk_choices = (
        (200, '200G'),
        (500, '500G'),
        (1000, '1T'),
        (2000, '2T'),
        (4000, '4T'),
        (8000, '8T'),
        (16000, '16T'),
    )

    ip = models.GenericIPAddressField(verbose_name='服务器IP')
    server = models.ForeignKey(Server, verbose_name='所属物理机')
    environ = models.ForeignKey(Environ, verbose_name='所属环境')
    project = models.ForeignKey(Project, verbose_name='所属项目')
    state = models.IntegerField(verbose_name='状态',choices=state_choices,default=0)
    os = models.ForeignKey(Os, verbose_name='操作系统')
    cpu = models.IntegerField(verbose_name='CPU', choices=cpu_choices,default=2)
    mem = models.IntegerField(verbose_name='内存', choices=mem_choices,default=2)
    disk = models.IntegerField(verbose_name='磁盘', choices=disk_choices,default=200)
    user = models.IntegerField(verbose_name='管理帐号',choices=user_choices,default=0)
    port = models.IntegerField(verbose_name='管理端口',choices=port_choices,default=0)
    remark = models.CharField(verbose_name='备注',max_length=256,blank=True)
    cdate = models.DateTimeField(verbose_name='申请时间',auto_now_add=True)


    def __str__(self):
        return self.ip




