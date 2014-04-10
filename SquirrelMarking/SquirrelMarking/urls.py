from django.conf.urls import patterns, include, url
from SquirrelMarking.views import login, student_home, lecturer_home, marker_home

urlpatterns = patterns('',
	(r'^$', login),
	(r'^student/$', student_home),
	(r'^lecturer/$', lecturer_home),
	(r'^marker/$', marker_home),
)