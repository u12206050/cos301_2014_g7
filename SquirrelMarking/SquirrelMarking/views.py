from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def login(request):
	t = get_template('login.html')
	html = t.render(Context())
	return HttpResponse(html)

def student_home(request):
	t = get_template('student.html')
	html = t.render(Context())
	return HttpResponse(html)
	
def lecturer_home(request):
	t = get_template('lecturer.html')
	html = t.render(Context())
	return HttpResponse(html)
	
def marker_home(request):
	t = get_template('marker.html')
	html = t.render(Context())
	return HttpResponse(html)