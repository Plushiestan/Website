"""plushiestan URL Configuration

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
from django.contrib import admin, auth
from django.urls import path, include

from home.views import homeView
from register.views import registerView
from eventcalendar.views import eventCalendarView

#from birthdays.views import birthdayAllView, birthdayDetailView, birthdayAddView, birthdayUpdateView

urlpatterns = [
    path('', homeView, name="home"),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', registerView, name='register'),
    path('travelagency/', include('travelagency.urls')),
    path('blog', include('blog.urls')),
    path('calendar/', eventCalendarView, name="calendar"),
    path('events/', include("events.urls")),
]

#path('polls/', include('polls.urls')),
#path('birthdays/', birthdayAllView, name="birthdays"),
#path('birthdays/add/', birthdayAddView, name="new-birthday"),
#path('birthdays/<int:eid>/update/', birthdayUpdateView, name="update-birthday"),
#path('birthdays/<int:eid>/details/<int:eid>', birthdayDetailView, name="birthday-details"),
