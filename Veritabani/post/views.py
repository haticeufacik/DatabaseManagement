from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib import messages

# Create your views here.


def post_index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'posts/detail.html', context)


def post_create(request):

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        messages.success(request, 'Sorunuz başarılı bir şekilde oluşturuldu!')
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form,
    }
    return render(request, 'posts/form.html', context)


def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, 'Sorunuz başarılı bir şekilde güncellendi!')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'posts/form.html', context)


def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('post:index')


def post(request):
    return HttpResponse('Burası post')
