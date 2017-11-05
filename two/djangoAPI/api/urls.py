from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.empty),
    url(r'.*', views.index)
]
