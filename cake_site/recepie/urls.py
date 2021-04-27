from django.urls import path

from . import views

urlpatterns = [
    path('<int:recepie_id>/', views.recepie_page, name='recepie_page'),
    path('', views.index, name='index'),
]
