from django.urls import path

from .views import AccordionView, CardView, HomeView, MarkdownView, SuperView, TabView


urlpatterns = [
    
    path('',  HomeView.as_view(), name='workshop'),
    path('accordion',  AccordionView.as_view(), name='accordion'),
    path('cards',  CardView.as_view(), name='cards'),
    path('tabs',  TabView.as_view(), name='tabs'),
    path('markdown',  MarkdownView.as_view(), name='markdown'),
    path('super',  SuperView.as_view(), name='super'),
    
]
