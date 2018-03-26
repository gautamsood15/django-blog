"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from articles import views
# from django_test import views
from articles.views import HelloTemplate
admin.autodiscover()


urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^hello/',views.hello,name='hello'),
    url(r'^hello_template/',views.hello_template,name='hello_template'),   
    url(r'^hello_template_simple/',views.hello_template_simple,name='hello_template_simple'),
    url(r'^hello_class_view/',HelloTemplate.as_view()),    
    url(r'^articles/',include('articles.urls')),
   url(r'^admin/',include(admin.site.urls)), 
   
   
   # user auth urls
    
    #url(r'^accounts/login/',views.login,name='login'),
    #url(r'^accounts/auth/',views.auth_views,name='auth_views'),
    #url(r'^accounts/logout/',views.logout,name='logout'),
    #url(r'^accounts/loggedin/',views.loggedin,name='loggedin'),
    #url(r'^accounts/invalid_login/',views.invalid_login,name='invalid_login'),
    #url(r'^accounts/register/',views.register_user,name='register_user'),
    #url(r'^accounts/register_success/',views.register_success,name='register_success'),
    
    
]  

