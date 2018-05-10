from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse

from authiz.models import Client
from .decorators import login_required

# Create your views here.

@login_required()
def profile(request):
    context = {
        'title': _('Мой профиль'),
        'user': Client.objects.filter(public_id=request.session.get('is_logged_in'))
    }
    return render(request, 'personal-area.html', context)

@login_required()
def treatments(request):
    context = {
        'title': _('Мое лечение'),
        'user': Client.objects.filter(public_id=request.session.get('is_logged_in'))
    }
    return render(request, 'personal-area-my-treatment.html', context)

@login_required()
def history(request):
    context = {
        'title': _('Моя история'),
        'user': Client.objects.filter(public_id=request.session.get('is_logged_in'))
    }
    return render(request, 'personal-area-visit-history.html', context)

@login_required()
def laboratory(request):
    context = {
        'title': _('Лабораторные анализы'),
        'user': Client.objects.filter(public_id=request.session.get('is_logged_in'))
    }
    return render(request, 'laboratory.html', context)

@login_required()
def booking_first_step(request):
    context = {
        'title': _('Запись к врачу'),
        'user': Client.objects.filter(public_id=request.session.get('is_logged_in'))
    }
    return render(request, 'personal-area-check-in-step1.html', context)