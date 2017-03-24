from django.conf.urls import url
from . import views
import bcrypt

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.create_user),
    url(r'^quotes$', views.quotes),
    url(r'^session$', views.login_user),
    url(r'^logout$', views.logout),
    url(r'^submit_quote$', views.submit_quote),
    url(r'^users/(?P<id>\d+)$', views.show)
]
