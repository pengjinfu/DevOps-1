# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from django.urls import path
from ..api import location as LOCATIONAPI

urlpatterns = [
    path(r'v1/location/', LOCATIONAPI.INFOLOCATIONListAPI.as_view()),
    path(r'v1/location/create/', LOCATIONAPI.INFOLOCATIONCreateAPI.as_view()),
    path(r'v1/location/<uuid:pk>/delete/', LOCATIONAPI.INFOLOCATIONDeleteAPI.as_view()),
]
