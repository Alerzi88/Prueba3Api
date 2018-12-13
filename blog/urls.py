from django.conf.urls import url
from blog.views import ClienteViewsets,OrdenViewsets,TecnicoViewsets
from django.urls import path
#from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('tecnico/', ClienteViewsets.as_view(), name='clientview'),
    path('cliente/', TecnicoViewsets.as_view(), name='tecnicoview'),
    path('orden/', OrdenViewsets.as_view(), name='ordenview'),
] 