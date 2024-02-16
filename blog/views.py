from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Post, Category
from django.views import View
from blog.models import Category, Post, PostComment


# Create your views here.
class PostListview(ListView):
    model = Post
    paginate_by = 1
    template_name = 'blog/index.html'

    def get_context_data(self, *args, **kwargs):
        posts = Post.objects.all()
        categories = Category.objects.all()
        context = {
            'posts': posts,
            'categories': categories
        }
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        post: Post = kwargs.get('object')
        context = {
            'comments': PostComment.objects.filter(approved=True, parent=None, post_id=post.id).prefetch_related(
                'postcomment_set'),
            'categories': Category.objects.all()
        }
        return context
    #
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     post_id = kwargs.get('post_id')  # دریافت شناسه پست از ورودی‌ها
    #     #todo i cant show the comments of this post
    #     # اضافه کردن اطلاعات به context
    #     context.update({
    #         'categories': Category.objects.all(),
    #         'comments': PostComment.objects.filter(approved=True, parent=None, post_id=post_id)
    #         # 'comments': list(PostComment.objects.all())
    #     })
    #     # print(post_id)
    #     return context
