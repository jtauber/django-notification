from django.conf.urls.defaults import *

from notification.views import notices, mark_all_seen, feed_for_user, single, notice_settings, archive

urlpatterns = patterns("",
    url(r'^$', notices, {'archived' : False }, name="notification_notices"),
    url(r'^all/$', notices, {'archived' : True }, name="notification_notices_all"),
    url(r'^settings/$', notice_settings, name="notification_notice_settings"),
    url(r'^(\d+)/$', single, name="notification_notice"),
    url(r'^(\d+)/archive/$', archive, {'next_page' : "../.." }, name="notification_archive"),
    url(r'^feed/$', feed_for_user, name="notification_feed_for_user"),
    url(r'^mark_all_seen/$', mark_all_seen, name="notification_mark_all_seen"),
)
