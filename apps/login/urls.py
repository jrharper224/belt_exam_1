from django.conf.urls import url
from . import views
import bcrypt

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.create_user),
    url(r'^success$', views.success),
    url(r'^session$', views.login_user)
]
