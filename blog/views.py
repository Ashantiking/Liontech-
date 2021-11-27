
from django.db import models
from django.shortcuts import render,  get_object_or_404
from django.urls.base import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post  # , Category
from .forms import PostForm, EditForm
from django.http import HttpResponseRedirect
# Create your views here.


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.like.add(request.user)
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class BlogView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    ordering = ['-publication_date']


# def CategoryView(request, cats):
#    category_posts = Post.objects.filter(category=cats)
#    return render(request, 'categories.html', {'cats': cats.title(), 'category_posts': category_posts})


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_details.html'

    def get_context_data(self, *args, **kwargs):
        #        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data()

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        #context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'


# class AddCategoryView(CreateView):
#    model = Category
    #form_class = PostForm
#    template_name = 'add_category.html'
#    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog')
