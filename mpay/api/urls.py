from django.contrib import admin
from django.urls import path, include
from mpay.api.views import LNMCallbackAPIView
urlpatterns = [
    path('lnm/', LNMCallbackAPIView.as_view(), name ='lnm-callbackurl'),
]