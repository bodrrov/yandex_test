from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('<username>/delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('<username>/edit/<int:post_id>/', views.post_edit, name='post_edit'),
    path('group/<slug:slug>/', views.group_posts, name='group'),
    path('new/', views.new_post, name='new-post'),
    path('follow/', views.follow_index, name='follow_index'),
    path('<str:username>/follow/', views.profile_follow,
         name="profile_follow"),
    path('<str:username>/unfollow/', views.profile_unfollow,
         name='profile_unfollow'),
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/<int:post_id>/comment/', views.add_comment,
         name='add_comment'),
    path('<str:username>/<int:post_id>/', views.post_view, name='post'),




]