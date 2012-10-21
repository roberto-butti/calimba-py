from django.conf.urls import patterns, include, url
import calimba.wiki.views

urlpatterns = patterns('calimba.wiki.views',
    # Examples:
    # url(r'^$', 'calimba.views.home', name='home'),
    # url(r'^calimba/', include('calimba.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', 'index'),
    
    url(r'(?P<page_slug>[^/]+)/edit/$', 'edit_page'),
    url(r'(?P<page_slug>[^/]+)/save/$', 'save_page'),
    url(r'(?P<page_slug>[^/]+)/$', 'view_page'),
)