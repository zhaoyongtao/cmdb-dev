#coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from . import forms
from models import *


def login(request):
    if request.method == 'POST':
        form = forms.Login_form(request.POST)

        if form.is_valid():
            user = form.cleaned_data['user']
            passwd1 = form.cleaned_data['passwd']

            # 帐号密码是否正确
            if User.objects.filter(user__exact=user, passwd__exact=passwd1).exists():
                row = User.objects.get(user=user)

                # 保存用户会话
                request.session['uid'] = row.id
                request.session['user'] = row.user
                request.session['lg_time'] = row.ll_date.strftime('%Y-%m-%d %H:%M')

                if request.session.get('remember') == 'y':
                    request.session.set_expiry(0)

                return render(request, 'op/index.html', {})
        else:
            return HttpResponse('内容不满足要求！')

    else:
        form = forms.Login_form()

    return render(request, 'account/login.html', {'form': form})


def logout(request):
    try:
        row = User.objects.get(user=request.session.get('user'))
        row.ll_date = timezone.now()
        row.save()
        request.session.flush()
    except KeyError:
        pass

    return HttpResponseRedirect(reverse('account:login'))


def register(request):
    if request.method == 'POST':
        form = forms.Register_form(request.POST)

        if form.is_valid():
            nickname = form.cleaned_data['nickname']
            user = form.cleaned_data['user']
            passwd1 = form.cleaned_data['passwd']
            email = form.cleaned_data['email']
            sex = int(form.cleaned_data['sex'])

            # 　是否已经被注册
            if User.objects.filter(nickname=nickname).exists():
                return HttpResponse('昵称：%s，已有人使用！' % nickname)
            else:
                if User.objects.filter(user=user).exists():
                    return HttpResponse('帐号：%s，已存在！' % user)
                else:
                    # 帐号写入数据库
                    row = User.objects.create(
                        nickname=nickname,
                        user=user,
                        passwd=passwd1,
                        email=email,
                        sex=sex
                    )

                    # 保存用户会话
                    request.session['uid'] = row.id
                    request.session['user'] = user
                    request.session['ll_date'] = timezone.now().strftime('%Y-%m-%d %H:%M')

                    return render(request, 'op/index.html', {})

    else:
        form = forms.Register_form()

    return render(request, 'account/register.html', {'form': form})

