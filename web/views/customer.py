#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：6/8/2020  10:21 PM 
# 文件名称   ：customer.py
from django.shortcuts import render


def customer_list(request):
    """
    客户信息列表
    :param request:
    :return:
    """
    return render(request, 'web/layout.html')
