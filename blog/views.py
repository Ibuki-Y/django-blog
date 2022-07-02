from django.shortcuts import redirect, render
from blog.forms import CommentForm
from .models import Post


def frontpage(request):
    posts = Post.objects.all()  # dbのPost情報を全て取得
    return render(request, "blog/frontpage.html", {"posts": posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():  # formが有効のとき
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_detail", slug=post.slug)

    else:
        form = CommentForm()

    return render(request, "blog/post_detail.html", {"post": post, "form": form})
