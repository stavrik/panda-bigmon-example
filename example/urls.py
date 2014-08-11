from django.conf import settings
from django.conf.urls import *
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.shortcuts import render_to_response
from django.template import RequestContext

common_patterns = patterns('',
    ### robots.txt
    url('^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

    ### the front page
#obsoleted.2014-05-01.jschovan#    url(r'^$', atlas_common_views.index, name='index'),
 #   url(r'^$', include('core.pandajob.urls_pandajob_mainpage')),

    url(r'^$', lambda request: render_to_response('_base_bigpandamon.html', {}, RequestContext(request)), name='index'),
 
    ### Applications
 #   url(r'^htcondorjobs', include('core.htcondor.urls')),
#obsoleted.2014-05-01.jschovan#    url(r'^job', include('core.pandajob.urls')),
 #   url(r'^jobs/', include('core.pandajob.urls_pandajob_jobs')),
 #   url(r'^job/', include('core.pandajob.urls_pandajob_singlejob')),
 #   url(r'^dash/', include('core.pandajob.urls_pandajob_dash')),
 #   url(r'^support/', include('core.pandajob.urls_pandajob_support')),

#obsoleted.2014-05-01.jschovan#    url(r'^u', include('core.pandajob.urls_users', namespace='user')),
 #   url(r'^users/', include('core.pandajob.urls_pandajob_users')),
 #   url(r'^user/', include('core.pandajob.urls_pandajob_singleuser')),

 #   url(r'^tasks/', include('core.pandajob.urls_pandajob_tasks')),
 #   url(r'^task/', include('core.pandajob.urls_pandajob_singletask')),

 #   url(r'^sites/', include('core.pandajob.urls_pandajob_sites')),
 #   url(r'^site/', include('core.pandajob.urls_pandajob_singlesite')),

 #   url(r'^resource', include('core.resource.urls')),
###     url(r'^api-auth', include('core.api.urls')),

    ### UI elements
 #   url(r'^api/datatables', include('core.table.urls')),
#    url(r'^graphics/', include('core.graphics.urls')),

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

