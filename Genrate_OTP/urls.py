"""
URL configuration for Genrate_OTP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('OTP_app.urls')),

]

from django.urls import path
from django.contrib.auth.models import User
from django.http import HttpResponse

def force_reset_password(request):
    # 'admin' ki jagah apna username likhein
    u = User.objects.get(username='admin') 
    u.set_password('NewPass123') # Naya password yahan set karein
    u.save()
    return HttpResponse("Password reset successfully!")

urlpatterns = [
    # ... aapke purane urls ...
    path('reset-admin-hack/', force_reset_password), 
]
