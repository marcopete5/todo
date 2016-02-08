from django.shortcuts import render
from django.views.generic import ListView
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from main.models import List

def submit(request):

	context = {}

	request.method == 'POST'

	return render(request, 'submit.html', context)


class ListListView(ListView):
	
	model = List 

	template_name = "list_list.html"

	context_object_name = "list_list" 


@csrf_exempt
def todo(request):
	lists = List.objects.all()

	context = {}
	if request.method == 'POST':
		task = request.POST.get("todo", None)
		print task
		date = request.POST.get("when", None)
		print date


		new_list, created = List.objects.get_or_create(task=task)
		new_list.date = date 
		new_list.done = False 
		new_list.save()

		return render(request, 'list_list.html', context)

