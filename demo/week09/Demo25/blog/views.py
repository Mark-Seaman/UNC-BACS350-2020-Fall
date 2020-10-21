from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy

from .models import Post


class BlogListView(ListView):
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
    
    
    
# Customize the views

# fields = '__all__'

# Use LoginRequiredMixin, 


# Use UserPassesTestMixin, 
#def test_func(self): 
#        obj = self.get_object()
#        return obj.author == self.request.user


#def form_valid(self, form):
#        form.instance.author = self.request.user
#        return super().form_valid(form)
#

# def get_context_data(self, **kwargs):
#        kwargs = super().get_context_data()
#        kwargs['title'] = 'Page Title'
#        return kwargs
