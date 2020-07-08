from django.urls import path
from learn_app import views

urlpatterns = [
    path('', views.index),
    path('i1',views.index1),
    path('i2',views.index2),
    path('temps',views.temps),
    path('temps2',views.temps2),
    path('data',views.data),
    ]
