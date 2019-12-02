"""App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.shortcuts import redirect

from .views import check_address, get_date_of_plan, NewPlanFormView

from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect

from . import views
app_name = 'app'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('planner/', permanent=False), name='planner'),
    path('users/', include('django.contrib.auth.urls')),
    path('planner/', include('planner.urls')),
    path('ajax/check_address/', check_address, name='check_address'),
    path('ajax/get-date-of-plan/', get_date_of_plan, name='get_date_of_plan'),
    path('new_plan', views.NewPlanFormView.as_view(), name='new_plan'),
]

if settings.DEBUG == True:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
