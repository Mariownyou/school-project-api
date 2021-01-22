from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index1'),
    path('news/', views.news, name='news'),
    path('new/', views.new_post, name='new'),
    path('new_category/', views.new_category, name='new_category'),
    path('group/<slug:slug>/', views.group, name='group'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('user/<str:username>/', views.profile, name='profile'),
    path('<str:username>/<int:post_id>/', views.post_view, name='post'),
    path(
        '<str:username>/<int:post_id>/edit/',
        views.post_edit,
        name='post_edit'
    ),
]
