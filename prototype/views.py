from django.shortcuts import render

# Create your views here.

from .models import User, Servicer, Meeting_location

def index(request):
	num_Users=User.objects.all().count()
	num_Servicer=Servicer.objects.all().count()
	num_Meeting_location=Meeting_location.objects.all().count()

	context={
		'num_Users': num_Users,
		'num_Servicers': num_Servicer,
		'num_Meeting_location': num_Meeting_location,
	}

	return render(request, 'index.html', context=context)

def show_map(request):
	context={}
	return render(request, 'default.html',context=context)


from django.views import generic

class UserListView(generic.ListView):
	model=User

class ServicerListView(generic.ListView):
	model=Servicer

class Meeting_locationListView(generic.ListView):
	model=Meeting_location