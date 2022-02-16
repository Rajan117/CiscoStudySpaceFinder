from django.urls  import  path
from MerakiApp import views

app_name = 'MerakiApp'

urlpatterns = [
    path('', views.user_dashboard, name='user-dashboard'),
    path('admin-home', views.admin_dashboard, name='admin-dashboard'),
    path('user-search', views.user_search, name='user-search'),
    path('user-results', views.user_results, name='user-results'),
    path('admin-login', views.admin_login, name='admin-login'),
    path('admin-alerts', views.admin_alerts, name='admin-alerts'),
    path('device/<slug:device_slug>', views.admin_device, name='admin-device')
]