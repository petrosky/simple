from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.views.generic import TemplateView


# Create your views here.


def index(request):
    tasks = Post.objects.all()
    return render(request, 'onemodel/index.html', {'tasks': tasks})


def add(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('onemodel/post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'onemodel/add.html', { 'form': form })


def post_detail(request, post_id):
    postid = request.GET('post_id')
    post = Post.objects(Post, pk=postid)
    return render(request, 'detail.html', {'post': post})




