from django.conf.urls import url
 
from club import views
 
app_name = 'club'
 
urlpatterns = [
 
    url(r'^$', views.IndexView.as_view(), name='index'),
 
    url(r'^club/entry/$',views.ClubEntry.as_view(),name='club-entry'),
 
]