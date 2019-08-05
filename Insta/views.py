from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import CustomUserCreationForm
from .models import InstaUser, Post

# Create your views here.
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "home.html"
    login_url = "login"

    # def get_queryset(self):
    #     current_user = self.request.user
    #     following = set()
    #     for conn in UserConnection.objects.filter(creator=current_user).select_related('following'):
    #         following.add(conn.following)
    #     return Post.objects.filter(author__in=following)

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "post_detail.html"
    login_url = "login"

    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     liked = Like.objects.filter(post=self.kwargs.get('pk'), user=self.request.user).first()
    #     if liked:
    #         data['liked'] = 1
    #     else:
    #         data['liked'] = 0
    #     return data

class PostCreateView(CreateView):
    model = Post
    template_name = "make_post.html"
    fields = '__all__'

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title']
    template_name = 'post_edit.html'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
