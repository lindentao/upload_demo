#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 #  @file       forms.py
 #  @brief      
 #  @version    1.0.0
 #  @author     LindenTao(lindentao@qq.com)
 #  @date       17/11/13 下午2:37
 #  @history    <author>    <time>    <desc>
 
"""

from django import forms


class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=50)
    file = forms.FileField()
