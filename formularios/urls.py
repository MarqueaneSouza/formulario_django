from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_forms, name='home_forms'),
    # path('processa_formulario', views.processa_formulario, name='processa_formulario'),
    path('processa_formulario_forms', views.processa_formulario_forms, name='processa_formulario_forms'),

]
