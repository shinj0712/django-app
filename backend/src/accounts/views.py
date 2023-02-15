from django.shortcuts import render
from django.views import generic

# Create your views here.

''' トップページ '''
class TopView(generic.TemplateView):
    template_name = 'accounts/login.html'