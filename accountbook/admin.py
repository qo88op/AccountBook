# -*- coding:utf-8 -*-
# __author__ = 'zsg'
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .models import Category, Bill, AccountUser
from django.contrib import admin


admin.site.register(Bill)
admin.site.register(Category)
admin.site.register(AccountUser)

