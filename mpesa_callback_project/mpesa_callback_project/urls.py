
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mpesa/', include('mpesa_callback_app.urls')),
]
