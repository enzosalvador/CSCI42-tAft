from django.urls import path
from . import views

# url for forum
urlpatterns = [
    path('', views.forum_view, name="forumposts"),
    path('forumposts/add', views.ForumPostCreateView.as_view(), name="forumpost_add" ),
    path('forumposts/<int:pk>/details', views.ForumPostDetailView.as_view(), name='forumpost_details'),
    path('forumposts/<int:pk>/edit', views.ForumPostUpdateView.as_view(), name='forumpost_edit'),
    path('forumposts/<int:post_pk>/reply/add', views.ReplyCreateView.as_view(), name="reply_add" ),
    path('forumposts/<int:post_pk>/reply/<int:reply_pk>/details', views.ReplyDetailView.as_view(), name="reply_details" ),
    path('forumposts/<int:post_pk>/reply/<int:reply_pk>/edit', views.ReplyUpdateView.as_view(), name="reply_edit" ),
]


app_name = "forum"