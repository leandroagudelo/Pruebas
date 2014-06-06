from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'inicio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'polls.views.home', name='home'),
    url(r'^save_poll/$', 'polls.views.save_poll', name='leandro'),
    url(r'^save_poll3/$', 'polls.views.save_poll_3', name='agudelo'),
)
