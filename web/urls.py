#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：6/8/2020  9:46 PM 
# 文件名称   ：urls.py
from django.conf.urls import url
from web.views import customer


urlpatterns = [
    # 客户信息管理
    url(r'customer/list/', customer.customer_list),
]
