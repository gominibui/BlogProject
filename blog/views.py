from django.shortcuts import render,get_object_or_404
# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from .models import Post
from .forms import CommentForm
from django.views import View



class StartingPageView(ListView):
    template_name = 'blog/index.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

class ALlPostView(ListView):
    template_name = 'blog/all-posts.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'all_posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset
        return data


class SinglePostView(View):
    def get(self, request,slug):
        post = Post.objects.get(slug=slug)
        context = {
            'post':post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all(),}
        return render(request, "blog/post-details.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post_detail-page", args=[slug]))

        context = {
            'post': post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all(),}


        return render(request, "blog/post-details.html", context)