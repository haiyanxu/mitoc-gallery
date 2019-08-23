from django.urls import path, include
from django.views.generic import TemplateView
from . import views
from .views import HomePageView

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    # url(r'^$', TemplateView.as_view(template_name='main.html'), name='home'),
]
