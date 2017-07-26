#coding=utf-8
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models


class User(models.Model):
    sex = (
        (1, '男',),
        (0, '女',)
    )

    nickname = models.CharField(verbose_name='昵称', max_length=64)
    user = models.CharField(verbose_name='用户', max_length=64)
    passwd = models.CharField(verbose_name='密码', max_length=64)
    email = models.EmailField(verbose_name='邮箱')
    sex = models.BooleanField(verbose_name='性别', choices=sex, default=1)
    cdate = models.DateTimeField(verbose_name='注册日期', auto_now_add=True)
    ll_date = models.DateTimeField(verbose_name='末次登录时间', auto_now=True)

    def __str__(self):
        return self.user