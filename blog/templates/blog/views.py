from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import (ListView ,
                                DetailView ,
                                CreateView,
                                UpdateView,
                                DeleteView)
from .models import Post

'''def home (request):

    context = {
        'notes':Post.objects.all(),
        'title':'home'
    }

    #return HttpResponse("<h1>This is the home page</h1>")
    return render(request,'eagle_note/home.html',context=context)

'''
class PostListView(ListView):
    model = Post
    template_name='eagle_note/home.html'
    context_object_name='notes'
    ordering=['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name='eagle_note/post_detail.html'
    context_object_name='notes'
    ordering=['-date_posted']


class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    

class PostDeleteView(LoginRequiredMixin,DeleteView,UserPassesTestMixin):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about (request):
    return render(request,'eagle_note/about.html',{'title':'about'})