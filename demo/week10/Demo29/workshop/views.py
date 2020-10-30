from django.views.generic import TemplateView
from markdown import markdown


text = '''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium quibusdam sit hic, ipsum labore commodi eligendi quos culpa maxime voluptate. Ad, voluptatem, esse! Quam accusantium minus sequi cumque minima quod odio accusamus assumenda dolorem consequuntur esse alias nisi, explicabo error! Dolores blanditiis adipisci laboriosam quo sequi nostrum consectetur recusandae illo sed molestias laborum, ullam modi doloremque. Facilis nulla iure odit accusamus. Doloremque voluptatibus repudiandae, beatae temporibus odit suscipit eius facere dolores quibusdam perspiciatis exercitationem velit porro cupiditate repellendus et tempora dolorem, sapiente, debitis cum nihil sunt. Illo perspiciatis cumque qui quia quam quibusdam doloribus fugiat porro, soluta esse nesciunt itaque? Blanditiis, voluptate, voluptates iure iste aut maxime perferendis aliquid, odit doloribus sapiente temporibus ad mollitia consequuntur, alias totam tenetur ut. Accusantium voluptas temporibus, ea a impedit.'''


class HomeView(TemplateView):
    template_name = 'workshop.html'

    
class CardView(TemplateView):
    template_name = 'cards.html'

    def get_context_data(self, **kwargs):
        data = dict(title="Life is Great", body=text)
        return dict(card=data)



#class CardsView(TemplateView):
#    template_name = 'cards.html'
#
#    def get_context_data(self, **kwargs):
#        return dict(cards=cards_data())



#def cards_data():
#    return [
#                dict(title="Card 1", body=text),
#                dict(title="Card 2", body=text),
#                dict(title="Card 3", body=text),
#            ]

#class MarkdownView(TemplateView):
#    template_name = 'markdown.html'
#
#    def get_context_data(self, **kwargs):
#        md_doc = "README.md"
#        return dict(markdown=markdown_data(md_doc))
#    
#class AccordionView(TemplateView):
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
#    
#def markdown_data(doc):
#    return dict(title=doc, html=markdown(open(doc).read()))
# 
    
def cards_data():
    return [
                dict(title="Card 1", body=text),
                dict(title="Card 2", body=text),
                dict(title="Card 3", body=text),
            ]
   
    
#def accordion_data():
#
#    def card_content(i, active):
#        card = dict(id=i, title=f'Week {i+1}', body=text)
#        if i == active:
#            card['show'] = 'show'
#            card['active'] = 'true'
#        return card
#
#    return [card_content(i, 0) for i in range(7)]
#
#
#def tabs_data():
#
#    def options(i, tab, selected):
#        if selected:
#            return dict(name=f'tab{i}', header=tab[0], body=tab[1],
#                        active='active', show='show', selected='true')
#        else:
#            return dict(name=f'tab{i}', header=tab[0], body=tab[1],
#                        active='', show='', selected='false')
#
#    tabs = ('Tab 1', text), ('Tab 2', text)
#    return [options(i, tab, i == 0) for i, tab in enumerate(tabs)]
#

