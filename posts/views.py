from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from posts.models import Post
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


from posts.forms import PostForm


@login_required
def create_post(request):
    """Create new post view."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )


class PostsFeedView(LoginRequiredMixin, ListView):
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 30
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'
