from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="home"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("patient_portal", views.patient_portal, name="patient_portal"),
    path("health_assis", views.health_assis, name="health_assistant"),
    path("contact", views.contact, name="contact"),
    path("logout", views.logout, name="logout"),
    path("verify-otp/", views.verify_otp, name="verify_otp"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
