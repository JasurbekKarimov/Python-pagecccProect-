from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import BackgroundImageForm



def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def set_background(request):
    if request.method == 'POST':
        form = BackgroundImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after successful upload
    else:
        form = BackgroundImageForm()
    return render(request, 'set_background.html', {'form': form})


class PagesaapListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

