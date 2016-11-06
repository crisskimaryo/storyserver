"""notesboard URL Configuration


The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Cla:ss-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, patterns, include
from django.contrib import admin
# from api.views import timetable ,updater ,calender,AuthView,RegView

from sb_api1.urls import router
from rest_framework.authtoken.views import obtain_auth_token




urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #api links
    url(r'^sb_api1/', include(router.urls)),
    # url(r'^api/token/', obtain_auth_token, name='api-token'),
    
    # #in future  link below should moved to another urls so that to give a clean arrangement
    # url(r'^api/auth/$',AuthView.as_view()),
    # url(r'^api/reg/$',RegView.as_view()),
    # # url(r'^api/timetable/$', timetable.as_view()),
   
    # # this are for rest_auth , from copy and paste

    # url(r'^rest-auth/', include('rest_auth.urls')),
    # url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),  
]