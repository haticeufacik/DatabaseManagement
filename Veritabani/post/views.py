from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# Create your views here.


def post_index(request):
    post_list = Post.objects.all()
    query = request.GET.get('q')
    if query:
        post_list = post_list.filter(
            Q(title__icontains=query) |
            Q(question_Content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        ).distinct()

    paginator = Paginator(post_list, 5)  # Show 5 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:

        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
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
