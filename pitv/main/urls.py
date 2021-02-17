from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from . import views
from . import api

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

    # API
    path('api/code/', api.code, name='pitv-api-code'),

    # Account
    path('account/', RedirectView.as_view(url=views.ACCOUNT_FIELDS[0].lower()), name='pitv-account'),
    path('account/devices/', views.account_devices, name='pitv-devices'),
    re_path(
        r'^account/devices/(?P<pk>\w+)/delete/$',
        view=views.CustomSessionDeleteView.as_view(),
        name='pitv-device-delete',
    ),
    path('account/edit/', views.account_edit, name='pitv-edit'),
    path('account/logout/', RedirectView.as_view(url='pitv-logout')),

    # Favicon
    path('favicon.ico', favicon_view)
]


