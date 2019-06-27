from django.http import HttpResponse
from django.shortcuts import render
from events.models import information




def index(request):
	infoList = information.objects.order_by('pk')
	context = {'infoList':infoList}
	return render(request, 'index.html', context)