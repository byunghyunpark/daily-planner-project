from django.conf.urls import url

from . import views





urlpatterns = [
    # 용필
    url(r'^index/$', views.index_schedule, name='index_schedule'),








    # 병현
    url(r'^score/$', views.score, name='score'),
    url(r'^add/schedule/$', views.add_schedule, name='add_schedule'),

]