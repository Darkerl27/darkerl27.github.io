from django.shortcuts import render,get_object_or_404
from .forms import CreateNewsForm
from .models import News,Category,Comment
from django.views import generic
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
# Create your views here.


class PostCreateView(generic.CreateView):
    form_class = CreateNewsForm
    template_name = 'post_new.html'
    success_url = reverse_lazy('home')


    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostListView(generic.ListView):
    model = News
    template_name = 'index.html'
    paginate_by = 1

class CategoryListView(generic.ListView):
    model = News
    template_name = 'category.html'
    paginate_by = 1
    def get_queryset(self):
        return News.objects.filter(is_published=True,category_id=self.kwargs['pk']).select_related('category')

class PostDetailView(generic.DetailView):
    model = News
    template_name = 'post_detail.html'
    def get_context_data(self, **kwargs):
        context=super(PostDetailView,self).get_context_data(**kwargs)
        stuff=get_object_or_404(News,id=self.kwargs['pk'])
        total_likes=stuff.total_likes()
        # total_subscribed=stuff.total_subscribe()
        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True
        # subscribed = False
        # if stuff.subscribe.filter(id=self.request.user.id).exists():
        #     subscribed = True
        #context['total_subscribed']=total_subscribed
        context['total_likes'] = total_likes
        context['liked']=liked
        #context['subscribed']=subscribed
        return context


class search(generic.ListView):

    template_name = 'home.html'
    paginate_by = 1

    def get_queryset(self):
        return News.objects.filter(title__icontains=self.request.GET.get('search'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['s']=f"search={self.request.GET.get('search')}&"
        return context


def like(requets,pk):
    post=get_object_or_404(News,id=requets.POST.get('post_id'))

    liked = False
    if post.likes.filter(id=requets.user.id).exists():
        post.likes.remove(requets.user)
        liked = False
    else:
        post.likes.add(requets.user)
        liked=True

    return HttpResponseRedirect(reverse('post_datail',args=[str(pk)]))