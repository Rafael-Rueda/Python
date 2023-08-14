from django.urls import path

from apps.trtvposts import views

app_name = 'trtvposts'

urlpatterns = [
    path('play/<slug:slug>', views.play, name='play'),
    path('comments/create_comment/<int:post_id>', views.create_comment, name='create_comment'),
    path('comments/delete_comment/<int:id>', views.delete_comment, name='delete_comment'),
    path('comments/like_comment/<int:comment_id>', views.likeacomment, name='like_comment'),
    path('comments/unlike_comment/<int:comment_id>', views.unlikeacomment, name='unlike_comment'),
]