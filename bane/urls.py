from django.conf.urls import url,include
from django.contrib import admin
from bane_was_bored import views as bane_views

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^tors/', bane_views.TorsList.as_view()),
    url(r'^posts/', bane_views.PostList.as_view()),
    url(r'^admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)
