from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from .models import *
from django.shortcuts import get_object_or_404

# dashboard view from .models
def forum_view(request):
    forumposts = ForumPost.objects.all()
    replies = Reply.objects.all()
    return render(request, 'forum/forum.html', {'forumposts': forumposts, 'replies': replies})
    

class ForumPostDetailView(DetailView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['replies'] = Reply.objects.all()
        return context
    
    model = ForumPost
    template_name = "forum/forumpost-details.html"  
       

class ForumPostCreateView(CreateView):
    model = ForumPost
    template_name = "forum/forumpost-add.html"
    fields = "__all__"

class ForumPostUpdateView(UpdateView):
    model = ForumPost
    template_name = "forum/forumpost-edit.html"
    fields = "__all__"


class ReplyDetailView(DetailView):
    model = Reply
    template_name = "forum/reply-details.html"

    # Override the `get_object` method to use 'reply_pk' from the URL parameters
    def get_object(self, queryset=None):
        # Use 'reply_pk' from `self.kwargs` to fetch the specific reply
        pk = self.kwargs.get('reply_pk')
        return get_object_or_404(Reply, pk=pk)
    

class ReplyCreateView(CreateView):
    model = Reply
    template_name = "forum/reply-add.html"
    fields = "__all__"
    def form_valid(self, form):
        form.instance.forum_post = ForumPost.objects.get(pk=self.kwargs['post_pk'])
        return super().form_valid(form)

class ReplyUpdateView(UpdateView):
    model = Reply
    template_name = "forum/reply-edit.html"
    fields = "__all__"
    def get_object(self, queryset=None):
        # Use 'reply_pk' from `self.kwargs` to fetch the specific reply
        pk = self.kwargs.get('reply_pk')
        return get_object_or_404(Reply, pk=pk)
