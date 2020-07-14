from django.http import HttpResponse
from django.views.generic import TemplateView


def index(request):
    return HttpResponse("<h1>Hello, world.</h1> <p>This is a simple HTML page.</p>")


class HomePageView(TemplateView):
    template_name = 'home.html'
    
