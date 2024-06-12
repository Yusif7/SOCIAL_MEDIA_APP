from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import PostCreateForm


@login_required
def post_create(request):
    if request.method == 'POST':
        post_form = PostCreateForm(data=request.POST, files=request.FILES)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.user = request.user
            new_post.save()
    else:
        post_form = PostCreateForm(data=request.GET)
    return render(request, 'create.html', {'post_form': post_form})
