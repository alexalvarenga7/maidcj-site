from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='index'),  # ← esta línea es clave
    path('services/', views.servicios, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('regular/', views.regular, name='Regular'),
    path('construction/', views.construction, name='Construction'),
    path('pre/', views.pre, name='pre'),
    path('comercial/', views.comercial, name='comercial'),
    path('inout/', views.inout, name='inout'),
]
