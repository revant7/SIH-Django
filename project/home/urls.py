from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("patient_portal", views.patient_portal, name="patient_portal"),
    path("logout", views.logout, name="logout"),
    path("verify-otp/", views.verify_otp, name="verify_otp"),
]
