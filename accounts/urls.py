from django.conf.urls import url, include
from . import urls_reset
from .views import index, register, profile, logout, login, home, how_to

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^index/$', index, name='index'),
    url(r'^home/$', home, name='home'),
    url(r'^how_to/$', how_to, name='how_to'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
]