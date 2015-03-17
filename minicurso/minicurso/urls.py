from django.conf.urls import patterns, include, url
from django.contrib import admin

from main.views import HomeView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'minicurso.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', HomeView.as_view()),

    url(r'^admin/', include(admin.site.urls)),
)
