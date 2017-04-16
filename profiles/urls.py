from django.conf.urls import url, include
from . import views

app_name = 'profiles'
urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^profile/(?P<username>[\w\-]+)/$', views.view_profile, name="view_profile"),
	url(r'^edit/(?P<userid>[\w\-]+)/$', views.edit_profile, name="edit_profile"),
	url(r'^recommend/$', views.recommend, name="recommend"),
	url(r'^indifferent/$', views.indifferent, name="indifferent"),
	url(r'^donotrecommend/$', views.do_not_recommend, name="donotrecommend"),
]