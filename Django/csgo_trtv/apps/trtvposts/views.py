from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from django.shortcuts import redirect, render

from apps.trtvposts.models import Comment, CommentLike, Post


def play(request, slug):
    post = Post.objects.filter(slug=slug).first()

    commentslikes = []
    for comment in post.comments.all():
        if CommentLike.objects.filter(comment=comment):
            commentslikes.append(
                (comment, len(CommentLike.objects.filter(comment=comment)))
            )
        else:
            commentslikes.append(
                (comment, '')
            )

    comments_liked = []
    for comment in post.comments.all():
        if CommentLike.objects.filter(comment=comment):
            for possible_like in CommentLike.objects.filter(comment=comment):
                if possible_like.author == request.user:
                    comments_liked.append(comment)

    if not post:
        raise Http404()
    return render(request, 'trtvposts/pages/play.html', context={'post': post, 'commentslikes': commentslikes, 'comments_liked': comments_liked})

def create_comment(request, post_id):
    content_type = ContentType.objects.get_for_model(Post)
    if request.POST.get('content'):
        if request.user.is_authenticated:
            Comment.objects.create(text=request.POST.get('content'), author=request.user, content_type=content_type, object_id=post_id)
        else:
            return redirect('authors:login')
    last_page = request.META.get('HTTP_REFERER')
    return redirect(last_page)

def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    if comment:
        comment.delete()
    last_page = request.META.get('HTTP_REFERER')
    return redirect(last_page)

def likeacomment(request, comment_id):
    if request.user.is_authenticated:
        comment = Comment.objects.get(id=comment_id)
        CommentLike.objects.create(comment=comment, author=request.user)
    else:
        return redirect('authors:login')
    last_page = request.META.get('HTTP_REFERER')
    return redirect(last_page)    

def unlikeacomment(request, comment_id):
    if request.user.is_authenticated:
        comment = Comment.objects.get(id=comment_id)
        CommentLike.objects.filter(comment=comment, author=request.user).first().delete()
    last_page = request.META.get('HTTP_REFERER')
    return redirect(last_page)    