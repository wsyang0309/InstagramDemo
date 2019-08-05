from django.urls import path

from Insta.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, SignUp

urlpatterns = [
    path('', PostListView.as_view(), name = 'home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post_detail'),
    path('post/new/', PostCreateView.as_view(), name = 'make_post'),
    path('post/edit/<int:pk>', PostUpdateView.as_view(), name='edit_post'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='delete_post'),
    path('auth/signup', SignUp.as_view(), name='sign_up'),
]