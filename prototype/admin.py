from django.contrib import admin
from .models import Servicer, User, Meeting_location

# Register your models here.

#admin.site.register(Servicer)
#admin.site.register(User)
#admin.site.register(Meeting_location)

#관리자를 위한 별도의 보기 처리
class ServicerAdmin(admin.ModelAdmin):
	list_display=('name', 'location', 'latitude', 'longitude')#관리자 사이트에서 목록보기
	fields = ['name', 'location', ('latitude', 'longitude')]#만들기 시 필드 레이아웃
admin.site.register(Servicer, ServicerAdmin)

class UserAdmin(admin.ModelAdmin):
	list_display=('name', 'location', 'latitude', 'longitude')
	fields = ['name', 'location', ('latitude', 'longitude')]
admin.site.register(User,UserAdmin)

class Meeting_locationAdmin(admin.ModelAdmin):
	list_display=('location', 'latitude', 'longitude')
	fields = ['location', ('latitude', 'longitude')]
admin.site.register(Meeting_location,Meeting_locationAdmin)