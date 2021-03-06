from django.conf.urls.defaults import *
from django.conf import settings
from django.conf import settings
from webcicletta.feeds import  *

site_feeds = {
        'blog':BlogFeed
}


urlpatterns = patterns('',
    (r'^$', 'webcicletta.views.index'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^admin/', include('django.contrib.admin.urls')),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/profile/$', 'webcicletta.views.profile'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    (r'^reord/$', 'webcicletta.views.test_reord'),
    (r'^blog/$', 'webcicletta.views.post_list'),
    (r'^blog/new/$', 'webcicletta.views.new_blog_post'),
    (r'^blog/(?P<slug>[-\w]+)/$', 'webcicletta.views.blog_post'),
    (r'^blog/(?P<slug>[-\w]+)/edit/$', 'webcicletta.views.edit_blog_post'),
    (r'^shows/$', 'webcicletta.views.shows'),
    (r'^showsgallery/$', 'webcicletta.views.showsgallery'),
    (r'^shows/(?P<slug>[-\w]+)/$', 'webcicletta.views.show_info'),
    (r'^change_current_show/$', 'webcicletta.views.change_current_show'),
    (r'^(?P<slug>[-\w]+)/$', 'webcicletta.views.page'),
    (r'^(?P<slug>[-\w]+)/edit/$', 'webcicletta.views.edit_page'),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',{'feed_dict':site_feeds})
    #(r'^feed/(?P<post_id>\d+)/rss/$', BlogFeed()),

)
