# -*- coding:utf-8 -*-
# __author__ = 'zsg'
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.conf.urls import url, include, patterns
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response, render


def test1(request):
    return render_to_response()


def test2(request):
    return render()


urlpatterns = [
    url('r^test1/$', test1),
    url('r^test2/$', test2),
]
