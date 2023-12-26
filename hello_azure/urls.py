from django.urls import path
from .views import index, predict

urlpatterns = [
    # path('predict/', views.index, name='predict'),
    # path('', views.index),
    # path(r'^predict/$', views.predict)
    path('', index, name='index'),
    path('predict/', predict, name='predict')
]