# -*- coding:utf-8 -*-
# __author__ = 'zsg'
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.six import python_2_unicode_compatible
from django_hstore import hstore
from .constants import BillType


def create_admin(*args, **kwargs):
    if User.objects.filter(username="admin"):
        return
    User.objects.create_superuser(username="admin", email="510185157@qq.com", password="123456")


signals.post_migrate.connect(create_admin)


@python_2_unicode_compatible
class AccountUser(User):
    preference = models.TextField(verbose_name="偏好", blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户管理"
        verbose_name_plural = verbose_name


@python_2_unicode_compatible
class Bill(models.Model):
    date = models.DateField(verbose_name="日期")
    amount = models.FloatField(verbose_name="金额")
    bill_type = models.IntegerField(verbose_name="类型", default=BillType.Expense.code,
                                         choices=BillType.all())
    remark = models.TextField(verbose_name="备注", blank=True)
    category = models.ForeignKey("Category", verbose_name="分类")
    data = hstore.DictionaryField(blank=True, verbose_name="数据")

    created = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    updated = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    objects = hstore.HStoreManager()

    @property
    def bill_type_name(self):
        return BillType.from_code(self.bill_type).description

    def __str__(self):
        return "账单:{0},{1}{2}元".format(self.date, self.bill_type_name, self.amount)

    class Meta:
        verbose_name = "记账本"
        verbose_name_plural = verbose_name


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(verbose_name="名称", max_length=100)
    data = hstore.SerializedDictionaryField(blank=True, verbose_name="数据")
    created = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    updated = models.DateTimeField(verbose_name='更新时间', auto_now=True)
    operator = models.CharField(max_length=50, verbose_name='操作员', blank=True)
    objects = hstore.HStoreManager()

    def __str__(self):
        return "分类:{}".format(self.name)

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name
