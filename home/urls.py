from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^data/', views.data, name = 'data'),
    url(r'^manufacturer/', views.manufacturer, name= 'manufacturer'),
    url(r'^notes/', views.notes, name= 'notes'),
]