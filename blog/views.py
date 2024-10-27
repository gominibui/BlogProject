from django.shortcuts import render,get_object_or_404
# Create your views here.

from .models import Post
from datetime import date
all_posts = [

]


def get_date(post):
    return post["date"]



def starting_page(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/index.html',
                  {'posts': latest_posts
                   })

def posts(request):
    all_posts_1 = Post.objects.all().order_by('-date')
    return render(request, 'blog/all-posts.html', {'all_posts': all_posts_1})



def post_detail(request, slug):
    # Получаем пост по slug, если не найдено, возвращаем 404
    indentified_post = get_object_or_404(Post, slug=slug)

    # Рендерим шаблон с найденным постом
    return render(request, 'blog/post-details.html', {
        'post': indentified_post,
        'post_tags': indentified_post.tags.all(),
    })

