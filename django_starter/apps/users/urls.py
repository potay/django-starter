from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
import views

# Main URL Patterns
urlpatterns = patterns('',
  url(r'^$', views.home, name='home'),
)
