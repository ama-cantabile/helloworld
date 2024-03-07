# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView, firstNamePageView, homePost, results


urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('amadeus/', firstNamePageView, name='amadeus'),
    path('homePost/', homePost, name='homePost'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),
]
