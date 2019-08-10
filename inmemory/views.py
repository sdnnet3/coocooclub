from django.shortcuts import render
from . models import People


# Create your views here.
def inMemory(request):
	people = People.objects.order_by('-passed')
	context = {'people':people}
	return render(request, 'inmemory/inmemory.html', context)