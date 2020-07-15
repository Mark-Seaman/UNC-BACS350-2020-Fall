from django.http import HttpResponse
from django.views.generic import TemplateView


def index(request):
    html = "<h1>Hello, world.</h1>" 
    html += ""<p>This is a simple HTML page.</p>"
    html += ""<p>This is a simple HTML page.</p>"
    return HttpResponse(html)


class HomePageView(TemplateView):
    template_name = 'home.html'
    

class IndexPageView(TemplateView):
    template_name = 'index.html'
