from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('photo', views.edit_photo, name='photo'),
    path('upload', views.upload_photo, name='upload'),
    path('logout', views.logout_view, name='logout'),
] 