from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from main.views import HomeView, CourseDetailView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'minicurso.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', HomeView.as_view()),
    url(r'^cursos/(?P<slug>[-\w]+)/$', CourseDetailView.as_view()),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$','django.views.static.serve',
            {'document_root':settings.MEDIA_ROOT,}
        ),
)
