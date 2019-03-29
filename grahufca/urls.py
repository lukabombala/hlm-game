from django.urls import path

from . import views

app_name = 'grahufca'
urlpatterns = [
    path('', views.index, name='index'),
    path('info', views.info, name='info'),
    path('vote/', views.vote, name='vote'),
]