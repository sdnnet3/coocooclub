from django.http import HttpResponse
from django.shortcuts import render
from . models import event




def eventPage(request):
	eventList = event.objects.order_by('-date')
	context = {'eventList':eventList}
	return render(request, 'events/twocolumn1.html', context)