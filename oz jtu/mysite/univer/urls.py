from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', include('dashboard.urls')),
    path('', views.index, name="index"),
    path('news/<int:news_id>/', views.news, name="news"),
    path('basic/<int:news_id>/', views.basic, name="basic"),
    # path('back_news/', views.back_news, name="back_news"),
    path('view/<int:pk>/', views.view, name="view"),
    path('search/', views.search, name="search"),
]
