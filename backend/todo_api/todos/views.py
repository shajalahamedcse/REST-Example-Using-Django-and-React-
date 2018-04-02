# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from django.shortcuts import render

from . import models
from . import serializers

# Create your views here.
class ListTodo(generics.ListCreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer