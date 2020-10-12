from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from .models import Superhero


#class HeroView(TemplateView):
#    template_name = "hero_detail.html"
#
#    def get_context_data(self, **kwargs):
#        hero = Superhero.objects.get(pk=1)
#        return {'hero': hero}


class HeroDetailView(DetailView):
    template_name = "hero_detail.html"
    model = Superhero
    
    
class HeroListView(ListView):
    template_name = "hero_list.html"
    model = Superhero
    
    
class HeroAddView(CreateView):
    template_name = "hero_add.html"
    model = Superhero
    fields = '__all__'
    
    
class HeroEditView(UpdateView):
    template_name = "hero_add.html"
    model = Superhero
    fields = '__all__'
    
    def get_context_data(self, **kwargs):
        kwargs = super(HeroEditView, self).get_context_data(**kwargs)
        kwargs['edit'] = True
        return kwargs
