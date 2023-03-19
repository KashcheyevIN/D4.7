from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import PostSearchForm


class PostsList(ListView):
    model = Post
    ordering = '-post_create_time'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostSearch(ListView):
    model = Post
    template_name = 'post_search.html'
    context_object_name = 'post_search'
    queryset = Post.objects.all().values().order_by('-id')
    paginate_by = 10
    form_class = PostSearchForm

    # Переопределяем функцию получения списка товаров
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #Забираем отфильтрованные объекты
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset()) #вписываем фильтр в контекст
        context['categories'] = Post.objects.all()
        context['form'] = PostSearchForm()
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class NewsCreate(CreateView):
    form_class = PostSearchForm
    model = Post
    template_name = 'news_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type_choice = 'NE'
        return super().form_valid(form)

class ArticleCreate(CreateView):
    form_class = PostSearchForm
    model = Post
    template_name = 'article_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type_choice = 'AR'
        return super().form_valid(form)

class NewsUpdate(UpdateView):
    form_class = PostSearchForm
    model = Post
    template_name = 'news_edit.html'

class ArticlesUpdate(UpdateView):
    form_class = PostSearchForm
    model = Post
    template_name = 'articles_edit.html'

class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('posts_list')

class ArticlesDelete(DeleteView):
    model = Post
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('posts_list')
