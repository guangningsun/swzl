"""apollo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from swzl import views
from django.conf.urls import include, url

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.init_web),
    url(r'^logout/', views.init_web),
    url(r'^create_user/', views.create_user),
    url(r'^get_all_user_info/', views.get_all_user_info),
    url(r'^user_login/', views.user_login),
    url(r'^get_user_info_by_id/', views.get_user_info_by_id),
    url(r'^modify_user/', views.modify_user),
    url(r'^remove_user/', views.remove_user),
   
    url(r'^manage_user', views.manage_user),
    url(r'^manage_lost', views.manage_lost),
    url(r'^manage_bus', views.manage_bus),
    url(r'^manage_type', views.manage_type),

    url(r'^get_all_type', views.get_all_type),
    url(r'^create_type', views.create_type),
    url(r'^remove_type', views.remove_type),
    url(r'^modify_type', views.modify_type),

    url(r'^create_bus_line', views.create_bus_line),
    url(r'^remove_bus_line', views.remove_bus_line),
    url(r'^get_all_bus_line', views.get_all_bus_line),
    url(r'^get_bus_line_by_name', views.get_bus_line_by_name),
    url(r'^modify_bus_line', views.modify_bus_line),

    url(r'^create_lost', views.create_lost),
    url(r'^remove_lost', views.remove_bus_line),
    url(r'^get_all_lost', views.get_all_lost),
    url(r'^get_lost_by_bus_line', views.get_lost_by_bus_line),
    url(r'^modify_lost', views.modify_lost),
    
    

]


handler404 = views.page_not_found