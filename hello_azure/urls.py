from django.urls import path
from .views import index, predict, language

urlpatterns = [
    # path('predict/', views.index, name='predict'),
    # path('', views.index),
    # path(r'^predict/$', views.predict)
    path('', index, name='index'),
    path('predict/', predict, name='predict'),
    path('index_CN.html', language, name='index_cn'),
    path('index.html', index, name='index_en')

]
