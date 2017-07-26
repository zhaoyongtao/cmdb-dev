#coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from . import forms
from models import *


def index(request):
    if request.session.get('user', ''):
        return render(request, 'op/index.html', {})
    else:
        return HttpResponseRedirect(reverse('Account:login'))


def env(request):
    if request.session.get('user',''):
        env = Environ.objects.all()
        return render(request, 'op/env.html', {'env': env})
    else:
        return HttpResponseRedirect(reverse('account:login'))

def env_add(request):
    if request.session.get('user',''):
        if request.method == 'POST':
            form = forms.Environ_form(request.POST)
            if form.is_valid():
                env_name = form.cleaned_data['env_name']
                if Environ.objects.filter(env_name=env_name).exists():
                    return HttpResponse('%s 已存在！' % env_name)
                else:
                    Environ.objects.create(
                        env_name=form.cleaned_data['env_name'],
                        description=form.cleaned_data['description'],
                    )
                    return HttpResponseRedirect(reverse('op:env'))
        else:
            form = forms.Environ_form()
        return render(request, 'op/env_add.html', {'form':form})
    else:
        return HttpResponseRedirect(reverse('account:login'))

def env_edit(request,id=''):
    if request.session.get('user',''):
        if request.method == 'GET':
            if id:
                row = get_object_or_404(Environ, id=id)
                data = {
                    'env_name':row.env_name,
                    'description':row.description,
                }
                form = forms.Environ_form(initial=data)
                return render(request, 'op/env_edit.html', {'form':form, 'id':id})


        if request.method == 'POST':
            form = forms.Environ_form(request.POST)
            if form.is_valid():
                Environ.objects.filter(id=id).update(
                    env_name=form.cleaned_data['env_name'],
                    description=form.cleaned_data['description'],
                )
                return HttpResponseRedirect(reverse('op:env'))

    else:
        return HttpResponseRedirect(reverse('account:login'))

def env_del(request,id=''):
    if request.session.get('user',''):
        Environ.objects.get(id=id).delete()
        return HttpResponseRedirect(reverse('op:env'))
    else:
        return HttpResponse('你没有权限那么做！')


def os(request):
    if request.session.get('user',''):
        os = Os.objects.all()
        return render(request, 'op/os.html', {'os': os})
    else:
        return HttpResponseRedirect(reverse('account:login'))

def os_add(request):
    if request.session.get('user',''):
        if request.method == 'POST':
            form = forms.Os_form(request.POST)

            if form.is_valid():
                os_name = form.cleaned_data['os_name']

                if Os.objects.filter(os_name=os_name).exists():
                    return HttpResponse('%s 已存在！' % os_name)
                else:
                    Os.objects.create(
                        os_name=form.cleaned_data['os_name'],
                        description=form.cleaned_data['description'],
                    )

                    return HttpResponseRedirect(reverse('op:os'))
        else:
            form = forms.Os_form()
        return render(request, 'op/os_add.html', {'form':form})
    else:
        return HttpResponseRedirect(reverse('account:login'))

def os_edit(request,id=''):
    if request.session.get('user',''):

        if request.method == 'GET':
            if id:
                row = get_object_or_404(Os, id=id)

                data = {
                    'os_name':row.os_name,
                    'description':row.description,
                }

                form = forms.Os_form(initial=data)

                return render(request, 'op/os_edit.html', {'form':form, 'id':id})


        if request.method == 'POST':
            form = forms.Os_form(request.POST)

            if form.is_valid():
                Os.objects.filter(id=id).update(
                    os_name=form.cleaned_data['os_name'],
                    description=form.cleaned_data['description'],
                )

                return HttpResponseRedirect(reverse('op:os'))

    else:
        return HttpResponseRedirect(reverse('account:login'))

def os_del(request,id=''):
    if request.session.get('user',''):
        Os.objects.get(id=id).delete()
        return HttpResponseRedirect(reverse('op:os'))
    else:
        return HttpResponse('你没有权限那么做！')


def project(request):
    if request.session.get('user',''):
        project = Project.objects.all()
        return render(request, 'op/project.html', {'project': project})
    else:
        return HttpResponseRedirect(reverse('account:login'))

def project_add(request):
    if request.session.get('user',''):
        if request.method == 'POST':
            form = forms.Project_form(request.POST)

            if form.is_valid():
                unit = form.cleaned_data['unit']

                if Project.objects.filter(unit=unit).exists():
                    return HttpResponse('%s 已存在！' % unit)
                else:
                    Project.objects.create(
                        project_name=form.cleaned_data['project_name'],
                        unit=form.cleaned_data['unit'],
                        manager=form.cleaned_data['manager'],
                        architect=form.cleaned_data['architect'],
                        developer=form.cleaned_data['developer'],
                        owner=User.objects.get(id=request.session.get('uid', '')),
                        git=form.cleaned_data['git'],
                        remark=form.cleaned_data['remark'],
                    )

                    return HttpResponseRedirect(reverse('op:project'))
            else:
                return HttpResponse('表单不通过！')
        else:
            form = forms.Project_form()

        return render(request, 'op/project_add.html', {'form':form})

    else:
        return HttpResponseRedirect(reverse('account:login'))

def project_edit(request,id=''):
    if request.session.get('user',''):
        if request.method == 'GET':
            if id:
                row = get_object_or_404(Project, id=id)

                data = {
                    'project_name':row.project_name,
                    'unit':row.unit,
                    'manager': row.manager,
                    'architect':row.architect,
                    'developer':row.developer,
                    'git':row.git,
                    'remark':row.remark,
                }

                form = forms.Project_form(initial=data)

                return render(request, 'op/project_edit.html', {'form':form, 'id':id})


        if request.method == 'POST':
            form = forms.Project_form(request.POST)

            if form.is_valid():
                Project.objects.filter(id=id).update(
                    project_name=form.cleaned_data['project_name'],
                    unit=form.cleaned_data['unit'],
                    manager=form.cleaned_data['manager'],
                    architect=form.cleaned_data['architect'],
                    developer=form.cleaned_data['developer'],
                    git=form.cleaned_data['git'],
                    remark=form.cleaned_data['remark'],
                )

                return HttpResponseRedirect(reverse('op:project'))
            else:
                return HttpResponse('表单不满足要求！')
    else:
        return HttpResponseRedirect(reverse('account:login'))

def project_del(request,id=''):
    if request.session.get('user',''):
        Project.objects.get(id=id).delete()
        return HttpResponseRedirect(reverse('op:project'))
    else:
        return HttpResponse('你没有权限那么做！')

def project_auth_list(request):
    if request.session.get('user',''):
        project = Project.objects.filter(auth_status=0)
        return render(request, 'op/project_auth.html', {'project': project})
    else:
        return HttpResponseRedirect(reverse('account:login'))

def project_auth(request,id=''):
    if request.session.get('user',''):
        if request.method == 'GET':
            if id:
                row = get_object_or_404(Project, id=id)

                data = {
                    'auth_status':row.auth_status,
                    'project_name':row.project_name,
                    'unit':row.unit,
                    'manager': row.manager,
                    'architect':row.architect,
                    'developer':row.developer,
                    'git':row.git,
                    'remark':row.remark,
                }

                form = forms.Project_auth_form(initial=data)

                return render(request, 'op/project_auth_edit.html', {'form':form, 'id':id})


        if request.method == 'POST':
            form = forms.Project_auth_form(request.POST)

            if form.is_valid():
                Project.objects.filter(id=id).update(
                    auth_status=form.cleaned_data['auth_status'],
                    project_name=form.cleaned_data['project_name'],
                    unit=form.cleaned_data['unit'],
                    manager=form.cleaned_data['manager'],
                    architect=form.cleaned_data['architect'],
                    developer=form.cleaned_data['developer'],
                    superviser=User.objects.get(id=request.session.get('uid', '')),
                    git=form.cleaned_data['git'],
                    remark=form.cleaned_data['remark'],
                )

                return HttpResponseRedirect(reverse('op:project_auth_list'))
    else:
        return HttpResponseRedirect(reverse('account:login'))


def resource(request):
    if request.session.get('user',''):
        resource = Resource.objects.all()
        return render(request, 'op/resource.html', {'resource': resource})
    else:
        return HttpResponseRedirect(reverse('account:login'))

def resource_add(request):
    if request.session.get('user',''):
        if request.method == 'POST':
            form = forms.Resource_form(request.POST)

            if form.is_valid():
                project = form.cleaned_data['project']

                if Resource.objects.filter(project=project).exists():
                    return HttpResponse('%s 已存在！' % project)
                else:
                    Resource.objects.create(
                        project=form.cleaned_data['project'],
                        environ=form.cleaned_data['environ'],
                        purpose=form.cleaned_data['purpose'],
                        apply_user=form.cleaned_data['apply_user'],
                        cpu=form.cleaned_data['cpu'],
                        mem=form.cleaned_data['mem'],
                        disk=form.cleaned_data['disk'],
                        os=form.cleaned_data['os'],
                        number=form.cleaned_data['number'],
                    )

                    return HttpResponseRedirect(reverse('op:resource'))
        else:
            form = forms.Resource_form()


        return render(request, 'op/resource_add.html', {'form':form})

    else:
        return HttpResponseRedirect(reverse('account:login'))

def resource_edit(request,id=''):
    if request.session.get('user',''):
        if request.method == 'GET':
            if id:
                row = get_object_or_404(Resource, id=id)

                data = {
                    'project':row.project,
                    'environ':row.environ,
                    'purpose': row.purpose,
                    'apply_user':row.apply_user,
                    'cpu':row.cpu,
                    'mem':row.mem,
                    'disk':row.disk,
                    'os':row.os,
                    'number':row.number,
                }

                form = forms.Resource_form(initial=data)

                return render(request, 'op/resource_edit.html', {'form':form, 'id':id})


        if request.method == 'POST':
            form = forms.Resource_form(request.POST)

            if form.is_valid():
                Resource.objects.filter(id=id).update(
                    project=form.cleaned_data['project'],
                    environ=form.cleaned_data['environ'],
                    purpose=form.cleaned_data['purpose'],
                    apply_user=form.cleaned_data['apply_user'],
                    cpu=form.cleaned_data['cpu'],
                    mem=form.cleaned_data['mem'],
                    disk=form.cleaned_data['disk'],
                    os=form.cleaned_data['os'],
                    number=form.cleaned_data['number'],
                )

                return HttpResponseRedirect(reverse('op:resource'))
    else:
        return HttpResponseRedirect(reverse('account:login'))

def resource_del(request,id=''):
    if request.session.get('user',''):
        Resource.objects.get(id=id).delete()
        return HttpResponseRedirect(reverse('op:resource'))
    else:
        return HttpResponse('你没有权限那么做！')

def resource_auth_list(request):
    if request.session.get('user',''):
        resource = Resource.objects.filter(auth_status=0)
        return render(request, 'op/resource_auth.html', {'resource': resource})
    else:
        return HttpResponseRedirect(reverse('account:login'))

def resource_auth(request,id=''):
    if request.session.get('user',''):

        # DB读取记录，并填充
        if request.method == 'GET':
            if id:
                row = get_object_or_404(Resource, id=id)

                data = {
                    'status':row.auth_status,
                    'project':row.project,
                    'environ':row.environ,
                    'purpose': row.purpose,
                    'apply_user':row.apply_user,
                    'cpu':row.cpu,
                    'mem':row.mem,
                    'disk':row.disk,
                    'os':row.os,
                    'number':row.number,
                }

                form = forms.Resource_auth_form(initial=data)

                return render(request, 'op/resource_auth_edit.html', {'form':form, 'id':id})

        # 记录写入DB
        if request.method == 'POST':
            form = forms.Resource_auth_form(request.POST)

            if form.is_valid():
                Resource.objects.filter(id=id).update(
                    auth_status =form.cleaned_data['auth_status'],
                    project=form.cleaned_data['project'],
                    environ=form.cleaned_data['environ'],
                    purpose=form.cleaned_data['purpose'],
                    apply_user=form.cleaned_data['apply_user'],
                    superviser=User.objects.get(id=request.session.get('uid', '')),
                    cpu=form.cleaned_data['cpu'],
                    mem=form.cleaned_data['mem'],
                    disk=form.cleaned_data['disk'],
                    os=form.cleaned_data['os'],
                    number=form.cleaned_data['number'],
                )

                return HttpResponseRedirect(reverse('op:resource_auth_list'))
    else:
        return HttpResponseRedirect(reverse('account:login'))


def server(request):
    if request.session.get('user',''):
        server = Server.objects.all()
        return render(request, 'op/server.html', {'server': server})
    else:
        return HttpResponseRedirect(reverse('account:login'))

def server_add(request):
    if request.session.get('user',''):
        if request.method == 'POST':
            form = forms.Server_form(request.POST)

            if form.is_valid():
                ip = form.cleaned_data['ip']

                if Server.objects.filter(ip=ip).exists():
                    return HttpResponse('%s 已存在！' % ip)
                else:
                    Server.objects.create(
                        ip=form.cleaned_data['ip'],
                        environ=form.cleaned_data['environ'],
                        project=form.cleaned_data['project'],
                        state=form.cleaned_data['state'],
                        os=form.cleaned_data['os'],
                        cpu=form.cleaned_data['cpu'],
                        mem=form.cleaned_data['mem'],
                        disk=form.cleaned_data['disk'],
                        user=form.cleaned_data['user'],
                        port=form.cleaned_data['port'],
                        remark=form.cleaned_data['remark']
                    )

                    return HttpResponseRedirect(reverse('op:server'))
        else:
            form = forms.Server_form()


        return render(request, 'op/server_add.html', {'form':form})

    else:
        return HttpResponseRedirect(reverse('account:login'))

def server_edit(request,id=''):
    if request.session.get('user',''):
        if request.method == 'GET':
            if id:
                row = get_object_or_404(Server, id=id)
                vhosts = Server.objects.get(id=id).vhost_set.all()

                data = {
                    'ip':row.ip,
                    'environ':row.environ,
                    'project':row.project,
                    'state':row.state,
                    'os': row.os,
                    'user':row.user,
                    'port':row.port,
                    'remark':row.remark,
                }

                form = forms.Server_form(initial=data)

                return render(request, 'op/server_edit.html', {'form':form, 'id':id, 'vhosts':vhosts})


        if request.method == 'POST':
            form = forms.Server_form(request.POST)

            if form.is_valid():
                Server.objects.filter(id=id).update(
                    ip=form.cleaned_data['ip'],
                    environ=form.cleaned_data['environ'],
                    project=form.cleaned_data['project'],
                    state=form.cleaned_data['state'],
                    os=form.cleaned_data['os'],
                    user=form.cleaned_data['user'],
                    port=form.cleaned_data['port'],
                    remark=form.cleaned_data['remark']
                )

                return HttpResponseRedirect(reverse('op:server'))
    else:
        return HttpResponseRedirect(reverse('account:login'))

def server_del(request,id=''):
    if request.session.get('user',''):
        Server.objects.get(id=id).delete()
        return HttpResponseRedirect(reverse('op:server'))
    else:
        return HttpResponse('你没有权限那么做！')


def vhost(request):
    if request.session.get('user',''):
        vhost = Vhost.objects.all()
        return render(request, 'op/vhost.html', {'vhost': vhost})
    else:
        return HttpResponseRedirect(reverse('account:login'))

def vhost_add(request):
    if request.session.get('user',''):
        if request.method == 'POST':
            form = forms.Vhost_form(request.POST)

            if form.is_valid():
                ip = form.cleaned_data['ip']

                if Vhost.objects.filter(ip=ip).exists():
                    return HttpResponse('%s 已存在！' % vip)
                else:
                    Vhost.objects.create(
                        ip=form.cleaned_data['ip'],
                        server=form.cleaned_data['server'],
                        project=form.cleaned_data['project'],
                        environ=form.cleaned_data['environ'],
                        state=form.cleaned_data['state'],
                        os=form.cleaned_data['os'],
                        user=form.cleaned_data['user'],
                        port=form.cleaned_data['port'],
                        remark=form.cleaned_data['remark']
                    )

                    return HttpResponseRedirect(reverse('op:vhost'))
        else:
            form = forms.Vhost_form()


        return render(request, 'op/vhost_add.html', {'form':form})

    else:
        return HttpResponseRedirect(reverse('account:login'))

def vhost_edit(request,id=''):
    if request.session.get('user',''):
        if request.method == 'GET':
            if id:
                row = get_object_or_404(Vhost, id=id)

                data = {
                    'ip':row.ip,
                    'server':row.server,
                    'project':row.project,
                    'environ':row.environ,
                    'state':row.state,
                    'os': row.os,
                    'user':row.user,
                    'port':row.port,
                    'remark':row.remark,
                }

                form = forms.Vhost_form(initial=data)

                return render(request, 'op/vhost_edit.html', {'form':form, 'id':id})


        if request.method == 'POST':
            form = forms.Vhost_form(request.POST)

            if form.is_valid():
                Vhost.objects.filter(id=id).update(
                    ip=form.cleaned_data['ip'],
                    environ=form.cleaned_data['environ'],
                    project=form.cleaned_data['project'],
                    state=form.cleaned_data['state'],
                    os=form.cleaned_data['os'],
                    user=form.cleaned_data['user'],
                    port=form.cleaned_data['port'],
                    remark=form.cleaned_data['remark']
                )

                return HttpResponseRedirect(reverse('op:vhost'))
    else:
        return HttpResponseRedirect(reverse('account:login'))

def vhost_del(request,id=''):
    if request.session.get('user',''):
        Vhost.objects.get(id=id).delete()
        return HttpResponseRedirect(reverse('op:vhost'))
    else:
        return HttpResponse('你没有权限那么做！')





