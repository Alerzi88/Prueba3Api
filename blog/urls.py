from django.conf.urls import url
from blog.views import ClienteViewSet, OrdenViewSet, 
from django.urls import path
#from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('tecnico/', ClienteViewSet.as_view(), name='clientlist'),
    path('cliente/', TecnicoViewSet.as_view(), name='tecnicolist'),
    path('orden/', OrdenViewSet.as_view(), name='ordenlist'),
] 