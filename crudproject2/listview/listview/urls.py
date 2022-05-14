"""listview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from termios import N_MOUSE
from django.contrib import admin
from django.urls import path
from portal import views
from enroll import views as enroll
from depart import views
urlpatterns = [
    path('admin/', admin.site.urls),
#    path('',enroll.StudentListView.as_view(),name='listview'),
 #   path('student/<int:pk>/',enroll.StudentDetailedView.as_view(),name='student_detail')   
 path('',views.ContactFormView.as_view(),name='home'),
 path('thankyou/',views.ThankYouView.as_view(),name='thanks')
]
