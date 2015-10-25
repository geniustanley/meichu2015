from django.contrib import admin
from Main.models import ReportList
from Main.models import ReportDetail
# Register your models here.

class ListAdmin(admin.ModelAdmin):
	list_display = ('id','reportname',)
class DetailAdmin(admin.ModelAdmin):
	list_display = ('listptr','latitude','longitude','time')

admin.site.register(ReportList, ListAdmin)
admin.site.register(ReportDetail, DetailAdmin)
