# comments/views.py

from django.shortcuts import render, redirect
from .models import Comment, User
from .forms import UserForm, CommentForm
from django.core.paginator import Paginator


SORT_FIELDS = {
    'username': 'user__username',
    'email': 'user__email',
    'date': 'created_at',
}


def comment_list(request):
    comments = Comment.objects.filter(parent__isnull=True).order_by('-created_at')
    paginator = Paginator(comments, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'comments/comment_list.html', {'page_obj': page_obj})

def add_comment(request):
    parent_id = request.GET.get('parent')
    parent_comment = Comment.objects.filter(id=parent_id).first() if parent_id else None

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        comment_form = CommentForm(request.POST)
        if user_form.is_valid() and comment_form.is_valid():
            user, _ = User.objects.get_or_create(
                username=user_form.cleaned_data['username'],
                email=user_form.cleaned_data['email'],
                homepage=user_form.cleaned_data.get('homepage')
            )
            comment = comment_form.save(commit=False)
            comment.user = user
            comment.parent = parent_comment
            comment.save()
            return redirect('comment_list')
    else:
        user_form = UserForm()
        comment_form = CommentForm()
    return render(request, 'comments/add_comment.html', {'user_form': user_form, 'comment_form': comment_form})
