from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader, RequestContext
from django.core.urlresolvers import reverse
from django.utils import timezone
from .models import blog

# Create your views here.
def login(request):
    template=loader.get_template('login.html')
    context = RequestContext(request,{'abs':1})
    return HttpResponse(template.render(context))

def home(request):
    template =loader.get_template('home.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def register(request):
    template =loader.get_template('register.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def blog_list(request):
    posts = blog.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    template = loader.get_template('login.html')
    context = RequestContext(request, {'posts': posts})
    return HttpResponse(template.render(context))