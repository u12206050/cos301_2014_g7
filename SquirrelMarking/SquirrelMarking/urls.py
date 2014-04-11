from django.conf.urls import patterns, include, url
from SquirrelMarking.views import login, student_home, lecturer_home, marker_home, assessment_view, assessment_manager, session_manager

urlpatterns = patterns('',
	(r'^$', login),
	(r'^student/$', student_home),
	(r'^lecturer/$', lecturer_home),
	(r'^marker/$', marker_home),
	(r'^assessmentView/$', assessment_view),
	(r'^assessmentManager/$', assessment_manager),
	(r'^sessionManager/$', session_manager),
)