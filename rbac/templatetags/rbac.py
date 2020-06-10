#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：6/11/2020  12:22 AM 
# 文件名称   ：rbac.py
from django.template import Library


register = Library()


@register.inclusion_tag('rbac/second_menu.html')
def second_menu(request):
    """
    二级菜单
    :param request:
    :return:
    """
    pass
