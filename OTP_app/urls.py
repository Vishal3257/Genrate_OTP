from django.urls import path
from OTP_app import views

urlpatterns = [
    path('api/register/', views.register, name='register'),
    path('api/send-otp/', views.send_otp, name='send_otp'),
    path('api/login-verify-otp/', views.login_verify_otp, name='login_verify_otp'),
    path('api/logout/', views.logout, name='logout'),
]



#https://vishalthakur3257-538610.postman.co/workspace/vishal-thakur's-Workspace~51ae67f4-cffc-48e5-869b-afef9b25e6bd/request/52549126-72b9609c-7161-463a-8044-49528d5af565?action=share&source=copy-link&creator=52549126&ctx=
#A4MhNpfn
#header name : x-api-key
#The API key for AUTH_API is: oZVCanOo.Usgly7tI1kpd0cW6Nrb42fKQ2VwK1oKm. Please store it somewhere safe: you will not be able to see it again.
# Authorization       Token   b5c6f50c395f47b9b1e59634102f47bf964935c9