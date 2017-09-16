from django.http import HttpResponse
from django.template import loader

def index(request):
	template = loader.get_template('parties/index.html')
	data = {}
	return HttpResponse(template.render(data, request))
