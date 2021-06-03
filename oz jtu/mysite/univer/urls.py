from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', include('dashboard.urls')),
    path('', views.index, name="index"),
    path('news/<int:news_id>/', views.news, name="news"),
    path('basic/<int:news_id>/', views.basic, name="basic"),
    path('view/<int:pk>/', views.view, name="view"),
    path('search/', views.search, name="search"),
    path('contact/', views.contact, name="contact"),
    path('teachers/', views.teacher, name="teachers"),
    path('quests/', views.quests, name="quests"),
]
