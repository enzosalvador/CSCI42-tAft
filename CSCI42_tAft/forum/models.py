from django.db import models
from django.urls import reverse
from userprofile.models import *


#Forum Model
class ForumPost(models.Model):
    title = models.CharField(max_length = 50)
    body = models.TextField(max_length = 1000)
    author = models.ForeignKey(UserProfileModel, on_delete = models.CASCADE)
    pub_datetime = models.DateTimeField("Published Date and Time", auto_now_add=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('forum:forumpost_details', kwargs={'pk':self.pk})
    
# Reply
# body; author; pub_datetime; forum_post;
class Reply(models.Model):
    body = models.TextField(max_length=1000)
    author = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE)
    pub_datetime = models.DateTimeField("Published Date and Time", auto_now_add=True)
    forum_post = models.ForeignKey(ForumPost, on_delete=models.CASCADE)

    def __str__(self):
        return self.body
    
    def get_absolute_url(self):
        return reverse('forum:reply_details', kwargs={'post_pk': self.forum_post.pk, 'reply_pk': self.pk})

