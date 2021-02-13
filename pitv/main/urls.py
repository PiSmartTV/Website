from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from . import views

favicon_path = staticfiles_storage.url('images/favicon.ico')
favicon_view = RedirectView.as_view(url=favicon_path, permanent=True)

urlpatterns = [
    # Misc
    path('', views.home, name='pitv-home'),
    path('not-available/', views.not_available, name='pitv-not-available'),

    # Users
    path('signup/', views.signup, name='pitv-signup'),
    path('login/', views.signin, name='pitv-login'),
    path('logout/', auth_views.LogoutView.as_view(), name='pitv-logout'),

    # Account
    path('account/', RedirectView.as_view(url=views.ACCOUNT_FIELDS[0].lower())),
    path('account/devices/', views.account_devices, name='pitv-devices'),

    # Favicon
    path('favicon.ico', favicon_view)
]
