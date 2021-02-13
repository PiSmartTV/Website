from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from . import views

favicon_path = staticfiles_storage.url('images/favicon.ico')
favicon_view = RedirectView.as_view(url=favicon_path, permanent=True)

urlpatterns = [
    path('', views.home, name='pitv-home'),
    path('signup/', views.signup, name='pitv-signup'),
    path('not-available/', views.not_available, name='pitv-not-available'),
    path('login/', views.signin, name='pitv-login'),
    path('logout/', auth_views.LogoutView.as_view(), name='pitv-logout'),

    # Favicon
    path('favicon.ico', favicon_view)
]
