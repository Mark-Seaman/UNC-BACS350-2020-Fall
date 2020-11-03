from django.urls import path

from .views import CardView, CardsView, DocumentView, HomeView


urlpatterns = [
    
    path('',  HomeView.as_view(), name='workshop'),
    
    path('card',  CardView.as_view(), name='card'),
    path('cards',  CardsView.as_view(), name='cards'),
    
    path('doc',  DocumentView.as_view(), name='doc'),
    
    
#    path('accordion',  AccordionView.as_view(), name='accordion'),
#    path('tabs',  TabView.as_view(), name='tabs'),
#    path('super',  SuperView.as_view(), name='super'),
    
]
