from django.shortcuts import render
from posts.models import Post

# Create your views here.


def index(request):
    post_list = Post.objects.all()
    return render(request, "index.html", {
        "posts": post_list,
    })
