from htmlmin.decorators import minified_response
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render, get_object_or_404, redirect

from .templatetags.filter import *
from urllib.parse import quote_plus
from .models import About, Team, Contact, Social, Treatment

# Create your views here.

@minified_response
def index(request):
    context = {
        'title':_('Главная'),
    }
    return render(request, 'index.html', context)

@minified_response
def faq(request):
    context = {
        'title':_('Вопросы-Ответы'),
    }
    return render(request, 'faq.html', context)

@minified_response
def about(request):
    context = {
        'title':_('О клинике'),
        'about':About.objects.order_by('-about').first(),
        'team':Team.objects.order_by('-fullname')
    }
    return render(request, 'about-us.html', context)

@minified_response
def contact(request):
    context = {
        'title':_('Контакты'),
        'contact':Contact.objects.order_by('-address').first(),
        'socials':Social.objects.all(),
    }
    return render(request, 'contacts.html', context)

@minified_response
def diagnostic(request):
    context = {
        'title':_('Диагностика'),
    }
    return render(request, 'diagnostics.html', context)

@minified_response
def treatment(request):
    context = {
        'title':_('Лечение'),
        'treatments':Treatment.objects.order_by('-publish'),
    }
    return render(request, 'treatment.html', context)

@minified_response
def treatment_inner(request, slug):
    treatment = get_object_or_404(Treatment, slug=slug)
    context = {
        'title':treatment.title,
        'treatment':treatment,
        'more_treatments':Treatment.objects.order_by('?').exclude(slug=slug)[0:6],
    }
    return render(request, 'treatment-inner.html', context)

@minified_response
def doctors(request):
    context = {
        'title':_('Врачи'),
    }
    return render(request, 'doctors.html', context)

@minified_response
def services(request):
    context = {
        'title':_('Услуги'),
    }
    return render(request, 'services.html', context)

@minified_response
def prices(request):
    context = {
        'title':_('Цены'),
    }
    return render(request, 'prices.html', context)