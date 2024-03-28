from django.contrib import admin
from django.urls import path, re_path, include
from courses import views
from rest_framework import routers


routers = routers.DefaultRouter()
#Lay duong dan tra ve
routers.register('categories', views.CategoryViewSet, basename='categories')
routers.register('courses', views.CourseViewSet, basename='courses')
routers.register('lessons',views.LessonViewSet, basename='lessons')


urlpatterns = [
    path('', include(routers.urls)),
]