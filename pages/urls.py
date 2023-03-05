# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView, semihPageView, results, homePost

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('semih/', semihPageView, name='semih'),
    path('homePost/', homePost, name='homePost'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),

]
