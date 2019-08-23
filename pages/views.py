from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# def home(request):
#     return render(request, 'main.html')
#
class HomePageView(TemplateView):
    template_name = 'main.html'
