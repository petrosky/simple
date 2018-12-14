from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Post
from django.utils import timezone
from .forms import PostForm



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
            return HttpResponseRedirect(reverse('onemodel:index'))
    else:
        form = PostForm()
        return render(request, 'onemodel/add.html', { 'form': form })


def post_detail(request, post_id):
    
    post = Post.objects(Post, pk=post_id)
    return render(request, 'detail.html', {'post': post})




