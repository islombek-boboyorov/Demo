from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_page, name="dashboard"),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),

    path('menu/', views.menu_list, name="menu_list"),
    path('menu/add/', views.menu_create, name="menu_add"),
    path('menu/<int:pk>/edit', views.menu_edit, name="menu_edit"),
    path('menu/<int:pk>/delete/', views.menu_delete, name="menu_delete"),

    path('basic/', views.basic_list, name="basic_list"),
    path('basic/add/', views.basic_create, name="basic_add"),
    path('basic/<int:pk>/edit/', views.basic_edit, name="basic_edit"),
    path('basic/<int:pk>/delete/', views.basic_delete, name="basic_delete"),

    path('category/', views.category_list, name="category_list"),
    path('category/add/', views.category_create, name="category_add"),
    path('category/<int:pk>/edit', views.category_edit, name="category_edit"),
    path('category/<int:pk>/delete/', views.category_delete, name="category_delete"),

    path('teacher/', views.teacher_list, name="teacher_list"),
    path('teacher/add/', views.teacher_create, name="teacher_add"),
    path('teacher/<int:pk>/edit/', views.teacher_edit, name="teacher_edit"),
    path('teacher/<int:pk>/delete', views.teacher_delete, name="teacher_delete"),

    path('news/', views.news_list, name="news_list"),
    path('news/add/', views.news_create, name="news_add"),
    path('news/<int:pk>/edit/', views.news_edit, name="news_edit"),
    path('news/<int:pk>/delete/', views.news_delete, name="news_delete"),
]
