from django.urls import path

from page.views import IndexPage, HomePage, BearPage


urlpatterns = [
    
    path('', IndexPage.as_view()),
    path('home', HomePage.as_view()),
    path('bear', BearPage.as_view()),
    
]
