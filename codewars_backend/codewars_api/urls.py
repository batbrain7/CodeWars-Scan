from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from codewars_api import views
# from django.contrib import admin

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^/$', views.SnippetList.as_view()),
    url(r'^Personal_Details/(?P<Barcode>[0-9]+)/$', views.personal_detail.as_view()),
    url(r'^Main_Details/(?P<Barcode>[0-9]+)/$', views.main_detail.as_view()),
    url(r'^Academic_Details/(?P<Barcode>[0-9]+)/$', views.academic_detail.as_view()),
    url(r'^Semester_1/(?P<Barcode>[0-9]+)/$', views.semester_1_detail.as_view()),
    url(r'^Semester_2/(?P<Barcode>[0-9]+)/$', views.semester_2_detail.as_view()),
    url(r'^Library/(?P<Barcode>[0-9]+)/$', views.library_detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
