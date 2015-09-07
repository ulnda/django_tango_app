from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('', 
  url(r'^$', views.index, name='index'),
  url(r'^categories/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
  url(r'^add_category/$', views.add_category, name='add_category'),
  url(r'^categories/(?P<category_name_slug>\w+)/add_page/$', views.add_page, name='add_page'),
  url(r'^register/$', views.register, name='register'),
  url(r'^logout/$', views.user_logout, name='logout'),
  url(r'^login/$', views.user_login, name='login'),)