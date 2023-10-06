from django.urls import path
from . import views

urlpatterns = [
    path('mpesa_callback/', views.mpesa_callback, name='mpesa_callback'),
]
