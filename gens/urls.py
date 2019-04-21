from django.urls import path
from . import views

urlpatterns = [
    path('', views.stranger, name='stranger'),
    path('stranger/', views.stranger, name='stranger'),
    path('soldier/', views.soldier, name='soldier'),
    path('trader/', views.trader, name='trader'),
    path('bandit/', views.bandit, name='bandit'),
    path('cultist/', views.cultist, name='cultist'),
    path('orc/', views.orc, name='orc'),
]
