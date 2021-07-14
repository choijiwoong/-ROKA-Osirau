from django.contrib import admin
from .models import Req_gui, Req_use, Meeting_location, Guide_info, User_info

# Register your models here.

class Req_guiAdmin(admin.ModelAdmin):
	list_display=('name', 'location', 'latitude', 'longitude', 'introduce')#관리자 사이트에서 목록보기
	fields = ['name', 'location', ('latitude', 'longitude'), 'introduce']#만들기 시 필드 레이아웃
admin.site.register(Req_gui, Req_guiAdmin)

class Req_useAdmin(admin.ModelAdmin):
	list_display=('name', 'location', 'latitude', 'longitude', 'introduce')
	fields = ['name', 'location', ('latitude', 'longitude'), 'introduce']
admin.site.register(Req_use,Req_useAdmin)

class Meeting_locationAdmin(admin.ModelAdmin):
	list_display=('location', 'latitude', 'longitude')
	fields = ['location', ('latitude', 'longitude')]
admin.site.register(Meeting_location,Meeting_locationAdmin)

class Guide_infoAdmin(admin.ModelAdmin):
	list_display=('name', 'password', 'email', 'identify_num')
	fields = [('name', 'password'), 'email', 'identify_num']
admin.site.register(Guide_info,Guide_infoAdmin)

class User_infoAdmin(admin.ModelAdmin):
	list_display=('name', 'password', 'email', 'dis_identify_num')
	fields = [('name', 'password'), 'email', 'dis_identify_num']
admin.site.register(User_info,User_infoAdmin)