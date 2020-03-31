"""api3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
"""from django.contrib import admin
from django.urls import path,include
from . import views
#namespace
app_name='home'
urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('confidence/',views.confidence,name='confidence'),
    path('academics/',views.academics,name='academics'),
    path('fitness/',views.fitness,name='fitness'),
    path('personality_development/',views.personality_development,name='personality_development'),
    path('home/',views.home,name='home'),
    path('login/',views.loginUser,name='login'),
    path('questionnare/',views.questionnare,name='questionnare'),
    path('logout/',views.logoutUser,name='logout'),
    path('attempt/',views.Attempt,name='attempt'),
    path('emailsent/',views.emailsent,name='emailsent'),
    path('addon/',views.addon,name='addon'),
    path('feedback/',views.feedback,name='feedback'),
    path('confidence/save_confi',views.save_confi,name='save_confi'),]
    """
"""api3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from . import views
#namespace
app_name='home'
urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('confidence/',views.confidence,name='confidence'),
    path('academics/',views.academics,name='academics'),
    path('fitness/',views.fitness,name='fitness'),
    path('personality_development/',views.personality_development,name='personality_development'),
    path('home/',views.home,name='home'),
    path('login/',views.loginUser,name='login'),
    path('questionnare/',views.questionnare,name='questionnare'),
    path('logout/',views.logoutUser,name='logout'),
    path('attempt/',views.Attempt,name='attempt'),
    path('addon/',views.addon,name='addon'),
    path('feedback/',views.feedback,name='feedback'),
    path('report/',views.report,name='report'),
    path('barg/',views.barg,name='barg'),
    path('certificate/',views.certificate,name='certificate'),
	path('mainpost/',views.getvalues,name='getvalues'),
    
    ]

