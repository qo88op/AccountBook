# -*- coding:utf-8 -*-
# __author__ = 'zsg'
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.conf.urls import url, patterns, include
from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.response import Response
from .models import Bill, Category, AccountUser


class BillSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)

    class Meta:
        model = Bill

class CategorySerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)

    class Meta:
        model = Category


class BillListCreateAPIView(ListCreateAPIView):
    serializer_class = BillSerializers

    def get_queryset(self):
        bills = Bill.objects.all()
        return bills

class CategoryListCreateAPIView(ListCreateAPIView):
    serializer_class = CategorySerializers

    def get_queryset(self):
        categorys = Category.objects.all()
        return categorys


urlpatterns = [
    url(r'bills/$', BillListCreateAPIView.as_view()),
    url(r'categorys/$', CategoryListCreateAPIView.as_view()),
]

