from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('',views.index, name='index'),

	path('sreq_gui/', views.req_guiListView.as_view(), name='sreq_gui'),
	path('Req_gui/<int:pk>', views.Req_guiDetailView.as_view(), name='Req_gui-detail'),
	path('sreq_use/', views.req_useListView.as_view(), name='sreq_use'),
	path('Req_use/<int:pk>', views.Req_useDetailView.as_view(), name='Req_use-detail'),

	path('meeting_locations/', views.Meeting_locationListView.as_view(), name='meeting_locations'),
	path('req_gui/new/', views.req_gui_new, name='req_gui_new'),
	path('req_use/new/', views.req_use_new, name='req_use_new'),

	path('unlogin_view/',views.unlogin_view, name='unlogin_view'),
	path('contact_view/',views.contact_view, name='contact_view'),

	path('register_gui/',views.register_gui, name='register_gui'),
	path('register_use/',views.register_use, name='register_use'),
]