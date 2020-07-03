from django.contrib import admin 
from django.urls import path , include
from tasks import views 

urlpatterns = [
    path("" ,views.index , name = "home"),
    path("update_task/<str:slug>/" , views.updatetask , name = "update_task"),
    path("delete_task/<str:slug>/" , views.delete_task , name = "delete_task"),

]
