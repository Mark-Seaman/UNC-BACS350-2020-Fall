from django.views.generic import TemplateView
from markdown import markdown

from .workshop import card_data, cards_data, markdown_data

class HomeView(TemplateView):
    template_name = 'workshop.html'

    
class CardView(TemplateView):
    template_name = 'card.html'

    def get_context_data(self, **kwargs):
        return dict(card=card_data())


class CardsView(TemplateView):
    template_name = 'cards.html'

    def get_context_data(self, **kwargs):
        return dict(cards=cards_data())


class DocumentView(TemplateView):
    template_name = 'markdown.html'

    def get_context_data(self, **kwargs):
        doc = "README.md"
        text = open(doc).read()
        card = card_data('Doc view', text, 'bg-danger', 'col-lg-12') 
        return dict(card=card)

    
# class AccordionView(TemplateView):
#    template_name = 'accordion.html'
#
#    def get_context_data(self, **kwargs):
#        return dict(accordion=accordion_data())
#
#    
#class TabView(TemplateView):
#    template_name = 'tabs.html'
#
#    def get_context_data(self, **kwargs):
#        return dict(tabs=tabs_data())
#    
#    
#
#class SuperView(TemplateView):
#    template_name = 'superview.html'
#
#    def get_context_data(self, **kwargs):
#        return dict(markdown=markdown_data('README.md'), 
#                    accordion=accordion_data(),
#                    cards=cards_data(),
#                    tabs=tabs_data())
#    

