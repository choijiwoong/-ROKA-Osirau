from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from django.contrib.auth.decorators import login_required, permission_required

from prototype.models import Req_gui, Req_use, Meeting_location, User_info, Guide_info
from .forms import Req_guiForm, Req_useForm, Regis_guideForm, Regis_userForm

from django.contrib.auth.models import User

def index(request):
	num_req_use=Req_use.objects.all().count()
	num_req_gui=Req_gui.objects.all().count()
	num_Meeting_location=Meeting_location.objects.all().count()

	req_guis=Req_gui.objects.all()
	req_uses=Req_use.objects.all()

	gui_lat=[]
	gui_long=[]
	for req_gui in req_guis:
		gui_lat.append(req_gui.latitude)
		gui_long.append(req_gui.longitude)

	use_lat=[]
	use_long=[]
	for req_use in req_uses:
		use_lat.append(req_use.latitude)
		use_long.append(req_use.longitude)

	context={
		'num_req_use': num_req_use,
		'num_req_gui': num_req_gui,
		'num_Meeting_location': num_Meeting_location,
		'gui_lat': gui_lat,
		'gui_long':gui_long,
		'use_lat': use_lat,
		'use_long':use_long,
	}
	return render(request, 'index.html', context=context)

def register_gui(request):
	if request.method=="POST":
		form=Regis_guideForm(request.POST)

		if form.is_valid():
			Guide_info=form.save(commit=True)
			Guide_info.name=form.cleaned_data['name']
			Guide_info.password=form.cleaned_data['password']
			Guide_info.email=form.cleaned_data['email']
			Guide_info.identify_num=form.cleaned_data['identify_num']

			user=User.objects.create_user(username=Guide_info.name, password=Guide_info.password, email=Guide_info.email)
			user.save()

			Guide_info.save()
			return redirect('index')
	else:
		form=Regis_guideForm()
	return render(request, 'register_guide.html', {'form':form})

def register_use(request):
	if request.method=="POST":
		form=Regis_userForm(request.POST)

		if form.is_valid():
			User_info=form.save(commit=True)
			User_info.name=form.cleaned_data['name']
			User_info.password=form.cleaned_data['password']
			User_info.email=form.cleaned_data['email']
			User_info.dis_identify_num=form.cleaned_data['dis_identify_num']

			user=User.objects.create_user(username=User_info.name, password=User_info.password, email=User_info.email)
			user.save()

			User_info.save()
			return redirect('index')
	else:
		form=Regis_userForm()
	return render(request, 'register_user.html', {'form':form})

def unlogin_view(request):
	context={}
	return render(request, 'Show_unlogin_home.html', context=context)

def contact_view(request):
	context={}
	return render(request, 'contact.html', context=context)

def req_gui_new(request):
	if request.method=="POST":
		form=Req_guiForm(request.POST)

		if form.is_valid():
			Req_gui=form.save(commit=True)
			Req_gui.name=form.cleaned_data['name']
			Req_gui.location=form.cleaned_data['location']
			Req_gui.latitude=form.cleaned_data['latitude']
			Req_gui.longitude=form.cleaned_data['longitude']
			Req_gui.introduce=form.cleaned_data['introduce']
			Req_gui.email=form.cleaned_data['email']
			Req_gui.save()
			return redirect('index')
	else:
		form=Req_guiForm()
	return render(request, 'prototype/req_gui_edit.html', {'form':form})

def req_use_new(request):
	if request.method=="POST":
		form=Req_useForm(request.POST)

		if form.is_valid():
			Req_use=form.save(commit=True)
			Req_use.name=form.cleaned_data['name']
			Req_use.location=form.cleaned_data['location']
			Req_use.latitude=form.cleaned_data['latitude']
			Req_use.longitude=form.cleaned_data['longitude']
			Req_use.introduce=form.cleaned_data['introduce']
			Req_gui.email=form.cleaned_data['email']
			Req_use.save()
			return redirect('index')
	else:
		form=Req_useForm()
	return render(request, 'prototype/req_use_edit.html', {'form':form})

class req_guiListView(generic.ListView):
	model=Req_gui
	paginate_by=5

	def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
		context = super(req_guiListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
		context['some_data'] = 'This is just some data'
		return context

class Req_guiDetailView(generic.DetailView):
	model=Req_gui
	paginate_by=5

class req_useListView(generic.ListView):
	model=Req_use

	def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
		context = super(req_useListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
		context['some_data'] = 'This is just some data'
		return context

class Req_useDetailView(generic.DetailView):
	model=Req_use
	paginate_by=5

class Meeting_locationListView(generic.ListView):
	model=Meeting_location

