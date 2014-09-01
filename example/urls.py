from django.conf import settings
from django.conf.urls import *
from django.conf.urls.static import static
from django.views.generic import TemplateView

common_patterns = patterns('',
    ### robots.txt
  #  url('^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

    ### the front page
   # url(r'^$', index, name='index'),
    url(r'^', include('core.common.common_urls')),


    ### Django Admin
    ### Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    ### Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    ### Django.js
    url(r'^djangojs/', include('djangojs.urls')),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns = patterns('',)
urlpatterns += common_patterns

#### django-debug-toolbar
#if settings.DEBUG:
#    import debug_toolbar
#    urlpatterns += patterns('',
#        url(r'^__debug__/', include(debug_toolbar.urls)),
#    )

