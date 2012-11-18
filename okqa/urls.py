from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

from registration.views import register

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^robots\.txt',
        TemplateView.as_view(template_name='robots.txt')
    ),

    url(r'', include('okqa.qa.urls')),
    url(r'', include('okqa.user.urls')),
    url(r'', include('social_auth.urls')),
    (r'^search/', include('okqa.search.urls')),
    (r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    # flat pages to help with static pages
    (r'^(?P<url>.*)$', 'django.contrib.flatpages.views.flatpage'),
)
