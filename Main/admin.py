from django.contrib import admin
from Main.models import ReportList
from Main.models import ReportDetail
# Register your models here.

class ListAdmin(admin.ModelAdmin):
	list_display = ('reportname',)
class DetailAdmin(admin.ModelAdmin):
	list_display = ('listptr','latitude','longtitude','time')

admin.site.register(ReportList, ListAdmin)
admin.site.register(ReportDetail, DetailAdmin)
