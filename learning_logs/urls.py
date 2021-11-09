"""Определяет схемы URL для learning_logs"""
# from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [

    # Домашняя страница
    re_path(r'^$', views.index, name='index'),

    # Вывод всех тем
    re_path('^topics/$', views.topics, name='topics'),

    # Страница с подробной информацией по отдельной теме
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # Страница для добавления новой темы
    path('new_topic/', views.new_topic, name='new_topic'),

    # Страница для добавления новой записи
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Страница для редактирования записей
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),

]
