from django.contrib import admin
from django.urls import path,include
from  thumbs_up import views

urlpatterns = [
    path('',views.intruduce_lend1),
    path("<int:pk>/",views.intruduceDetail.as_view()),
    path('like/',views.video_like , name = 'video_like'),
]
