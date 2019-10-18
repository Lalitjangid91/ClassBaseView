"""ClassBaseView URL Configuration

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
from BasicApp import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.Home.as_view()),
    path('school/',views.SchoolListView.as_view(),name='school'),
    path('school/<pk>/',views.SchoolDetailView.as_view(),name='detail'),
    path('student/',views.StudentListView.as_view(),name='student'),
    path('addschool/',views.SchoolCreate.as_view(),name='addschool'),
    path('addstudent/',views.StudentCreate.as_view(),name='addstudent'),
    path('deleteschool/',views.SchoolListView.as_view(),name='deleteschool'),
    path('deleteschool/<pk>/',views.SchoolDelete.as_view(),name='schooldelete'),
    path('deletestudent/',views.StudentData.as_view(),name='deletestudent'),
    path('deletestudent/<pk>/',views.StudentDelete.as_view(),name='studentdelete'),
    path('updateschool/',views.SchoolListView.as_view(),name='updateschool'),
    path('updateschool/<pk>/',views.SchoolUpdate.as_view(),name='schoolupdate'),
    path('updatestudent/',views.StudentData.as_view(),name='updatestudent'),
    path('updatestudent/<pk>/',views.StudentUpdate.as_view(),name='studentupdate'),


]
