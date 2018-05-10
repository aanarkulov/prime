"""prime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from main import views as main_views
from main.call_views import *
from authiz import views as auth_views
from cabinet import views as profile_views

urlpatterns = i18n_patterns(
    # Admin views
    url('admin/', admin.site.urls),

    url('i18n/', include('django.conf.urls.i18n')),
    # url(r'^i18n/setLang/', include('django.conf.urls.i18n')),

    # Main app url's
    url('home/', main_views.index, name='index'),
    url('faq/', main_views.faq, name='faq'),
    url('about', main_views.about, name='about'),
    url('contact/', main_views.contact, name='contact'),
    url('diagnostic/', main_views.diagnostic, name='diagnostic'),
    url('treatment/', main_views.treatment, name='treatment'),
    url(r'^treatments/(?P<slug>[^/]+)$', main_views.treatment_inner, name="treatment_inner"),
    url('doctors/', main_views.doctors, name='doctors'),
    url('services/', main_views.services, name='services'),
    url('prices/', main_views.prices, name='prices'),

    # Authiz app url's (login, logout, register)
    # url('auth/', auth_views.login , name='login'),
    url('auth/login', auth_views.login , name='login'),
    url('auth/register', auth_views.register , name='register'),
    url('auth/confirm', auth_views.code_activation , name='code_activation'),
    url('logout/', auth_views.log_me_out, name="log_me_out"),

    # Cabinet app url's
    url('profile/', profile_views.profile, name="profile"),
    url('cabinet/my-treatments/', profile_views.treatments, name="treatments"),
    url('cabinet/history/', profile_views.history, name="history"),
    url('cabinet/laboratory/', profile_views.laboratory, name="laboratory"),
    url('cabinet/booking/first', profile_views.booking_first_step, name="booking_first_step"),
)

# Another pattern for media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)