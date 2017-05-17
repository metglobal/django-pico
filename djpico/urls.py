from django.conf.urls import url
from djpico import views

urlpatterns = [
    url(r'pico.js|client.js', views.picojs, name='picojs'),
    url(r'^.*$', views.index, name='index'),
]
