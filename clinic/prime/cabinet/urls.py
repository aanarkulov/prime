from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.profile, name="profile"),
    path('my-treatments/', views.treatments, name="treatments"),
    path('history/', views.history, name="history"),
]