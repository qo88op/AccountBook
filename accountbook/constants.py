# -*- coding:utf-8 -*-
# __author__ = 'zsg'
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import enum


class EnumWithDescription(enum.Enum):
    def __init__(self, code, description):
        self.code, self.description = code, description

    @classmethod
    def all(cls):
        return [(e.code, e.description) for e in cls]

    @classmethod
    def from_code(cls, code):
        for obj in cls:
            if obj.code == code:
                return obj
        return None


class BillType(EnumWithDescription):
    Income = (1, "收入")
    Expense = (2, "支出")
