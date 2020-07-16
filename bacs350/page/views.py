from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'home.html'
    

class IndexPage(TemplateView):
    template_name = 'index.html'


class BearPage(TemplateView):
    template_name = 'bear.html'
    
