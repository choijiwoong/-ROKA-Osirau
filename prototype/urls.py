from django.urls import path
from . import views

urlpatterns = [
	path('',views.index, name='index'),#for make html

	path('',views.show_map, name='show_map'),

	path('users/', views.UserListView.as_view(), name='users'),
	path('servicers/', views.ServicerListView.as_view(), name='servicers'),
	path('meeting_locations/', views.Meeting_locationListView.as_view(), name='meeting_locations'),
]
