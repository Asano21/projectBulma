from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('all-news', views.allPost, name='allPost'),
    path('post/views/<int:pk>', views.postDetail, name='postDetail'),
    path('add-post', views.addPost, name='addPost'),
    path('post/delete/<int:pk>', views.deletePost, name='deletePost'),
    path('post/edit/<int:pk>', views.editPost, name='editPost')
]