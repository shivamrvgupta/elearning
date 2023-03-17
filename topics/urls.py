from django.urls import path
from  . import views

urlpatterns = [
    path('', views.index, name='topics'),
    path('<int:topic_id>/', views.topic, name='topic'),
    path('video', views.video, name='video'),
]
