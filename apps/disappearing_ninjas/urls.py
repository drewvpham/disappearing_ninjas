from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r"^ninjas/$", views.index),
    url(r"^ninjas/(?P<color>\w*)", views.show_ninja),
]
