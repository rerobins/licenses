
from django.conf.urls import url, patterns
from licenses.views import LicensedSoftwareListView

urlpatterns = patterns('',
                       url(r'^$', LicensedSoftwareListView.as_view(),
                           name='license_list'),
                       )