#coding=utf-8
from django import forms
from django.forms import ModelForm
from django.forms.widgets import TextInput, Textarea, Select, PasswordInput, EmailInput
from .models import *
from account.models import *


# 环境字典
class Environ_form(ModelForm):
    class Meta:
        model = Environ
        fields = ['env_name','description']
        widgets = {
            'env_name': TextInput(attrs={'class': 'form-control', 'placeholder': '测试'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': '描述性文字'})
        }


# 操作系统字典
class Os_form(ModelForm):
    class Meta:
        model = Os
        fields = ['os_name','description']
        widgets = {
            'os_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Redhat7'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': '描述性文字'})
        }

# 项目新增修改
class Project_form(ModelForm):
    class Meta:
        model = Project
        widgets = {
            'unit': TextInput(attrs={'class': 'form-control'}),
            'project_name': TextInput(attrs={'class': 'form-control'}),
            'manager': Select(attrs={'class': 'form-control'}),
            'architect': Select(attrs={'class': 'form-control'}),
            'developer': Select(attrs={'class': 'form-control'}),
            'git': TextInput(attrs={'class': 'form-control', 'placeholder': 'ssh://git@10.1.1.47:21312/~/devops.git'}),
            'remark': TextInput(attrs={'class': 'form-control'}),
        }
        fields = ['unit', 'project_name', 'manager', 'architect', 'developer', 'git', 'remark']

    manager = forms.ModelChoiceField(
        label=u'项目经理',
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    architect = forms.ModelChoiceField(
        label=u'架构师',
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    developer = forms.ModelChoiceField(
        label=u'开发人员',
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

# 项目审核
class Project_auth_form(ModelForm):
    class Meta:
        model = Project
        widgets = {
            'auth_status': Select(attrs={'class': 'form-control'}),
            'unit': TextInput(attrs={'class': 'form-control'}),
            'project_name': TextInput(attrs={'class': 'form-control'}),
            'manager': Select(attrs={'class': 'form-control'}),
            'architect': Select(attrs={'class': 'form-control'}),
            'developer': Select(attrs={'class': 'form-control'}),
            'git': TextInput(attrs={'class': 'form-control', 'placeholder': 'ssh://git@10.1.1.47:21312/~/devops.git'}),
            'remark': TextInput(attrs={'class': 'form-control'}),
        }
        fields = ['auth_status', 'unit', 'project_name', 'manager', 'architect', 'developer', 'git', 'remark']

    manager = forms.ModelChoiceField(
        label=u'项目经理',
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    architect = forms.ModelChoiceField(
        label=u'架构师',
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    developer = forms.ModelChoiceField(
        label=u'开发人员',
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )


# 资源新增修改
class Resource_form(ModelForm):
    class Meta:
        model = Resource
        widgets = {
            'environ': Select(attrs={'class': 'form-control'}),
            'purpose': TextInput(attrs={'class': 'form-control'}),
            'apply_user': Select(attrs={'class': 'form-control'}),
            'cpu': Select(attrs={'class': 'form-control'}),
            'mem': Select(attrs={'class': 'form-control'}),
            'disk': Select(attrs={'class': 'form-control'}),
            'os': Select(attrs={'class': 'form-control'}),
            'number': Select(attrs={'class': 'form-control'}),
        }
        fields = ['project', 'environ', 'purpose', 'apply_user', 'cpu', 'mem', 'disk', 'os', 'number']

    project = forms.ModelChoiceField(
        label=u'项目',
        queryset=Project.objects.filter(auth_status=1),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

# 资源审核
class Resource_auth_form(ModelForm):
    class Meta:
        model = Resource
        widgets = {
            'auth_status': Select(attrs={'class': 'form-control'}),
            'environ': Select(attrs={'class': 'form-control'}),
            'purpose': TextInput(attrs={'class': 'form-control'}),
            'apply_user': Select(attrs={'class': 'form-control'}),
            'cpu': Select(attrs={'class': 'form-control'}),
            'mem': Select(attrs={'class': 'form-control'}),
            'disk': Select(attrs={'class': 'form-control'}),
            'os': Select(attrs={'class': 'form-control'}),
            'number': Select(attrs={'class': 'form-control'}),
        }
        fields = ['auth_status', 'project', 'environ', 'purpose', 'apply_user', 'cpu', 'mem', 'disk', 'os', 'number']

    project = forms.ModelChoiceField(
        label=u'项目',
        queryset=Project.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )



# 物理机
class Server_form(ModelForm):
    class Meta:
        model = Server
        fields = ['ip','environ','project','state','os','cpu','mem','disk','user','port','remark']
        widgets = {
            'ip': TextInput(attrs={'class': 'form-control', 'placeholder': 'x.x.x.x'}),
            'environ': Select(attrs={'class': 'form-control'}),
            'project': Select(attrs={'class': 'form-control'}),
            'state': Select(attrs={'class': 'form-control'}),
            'os': Select(attrs={'class': 'form-control'}),
            'cpu': Select(attrs={'class': 'form-control'}),
            'mem': Select(attrs={'class': 'form-control'}),
            'disk': Select(attrs={'class': 'form-control'}),
            'user': Select(attrs={'class': 'form-control'}),
            'port': Select(attrs={'class': 'form-control'}),
            'remark': Textarea(attrs={'class': 'form-control', 'placeholder': ''})
        }


# 虚拟机
class Vhost_form(ModelForm):
    class Meta:
        model = Vhost
        fields = ['ip','server','environ','project','state','os','cpu','mem','disk','user','port','remark']
        widgets = {
            'ip': TextInput(attrs={'class': 'form-control', 'placeholder': 'x.x.x.x'}),
            'server': Select(attrs={'class': 'form-control'}),
            'environ': Select(attrs={'class': 'form-control'}),
            'project': Select(attrs={'class': 'form-control'}),
            'state': Select(attrs={'class': 'form-control'}),
            'os': Select(attrs={'class': 'form-control'}),
            'cpu': Select(attrs={'class': 'form-control'}),
            'mem': Select(attrs={'class': 'form-control'}),
            'disk': Select(attrs={'class': 'form-control'}),
            'user': Select(attrs={'class': 'form-control'}),
            'port': Select(attrs={'class': 'form-control'}),
            'remark': Textarea(attrs={'class': 'form-control', 'placeholder': ''})
        }







    
    
    
    
    
    
    
    
    
    