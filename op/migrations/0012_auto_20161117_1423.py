# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-17 14:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('op', '0011_auto_20161116_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='op.Project', verbose_name='\u6240\u5c5e\u9879\u76ee'),
        ),
        migrations.AddField(
            model_name='vhost',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='op.Project', verbose_name='\u6240\u5c5e\u9879\u76ee'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='op.Project', verbose_name='\u6240\u5c5e\u9879\u76ee'),
        ),
        migrations.AlterField(
            model_name='server',
            name='port',
            field=models.IntegerField(choices=[(0, 22), (1, 21312), (2, 21212), (3, 53977)], default=0, verbose_name='\u7ba1\u7406\u7aef\u53e3'),
        ),
        migrations.AlterField(
            model_name='server',
            name='user',
            field=models.IntegerField(choices=[(0, 'root'), (1, 'developer'), (2, 'test')], default=0, verbose_name='\u7ba1\u7406\u5e10\u53f7'),
        ),
        migrations.AlterField(
            model_name='vhost',
            name='port',
            field=models.IntegerField(choices=[(0, 22), (1, 21312), (2, 21212), (3, 53977)], default=0, verbose_name='\u7ba1\u7406\u7aef\u53e3'),
        ),
        migrations.AlterField(
            model_name='vhost',
            name='user',
            field=models.IntegerField(choices=[(0, 'root'), (1, 'developer'), (2, 'test')], default=0, verbose_name='\u7ba1\u7406\u5e10\u53f7'),
        ),
    ]
