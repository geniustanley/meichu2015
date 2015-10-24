from django.shortcuts import render_to_response
from Main.models import ReportList
from Main.models import ReportDetail
from django.template import RequestContext
from time import strftime
# Create your views here.


def MainPageList(request):	

	RList = ReportList.objects.all()
	return render_to_response('index.html',RequestContext(request,locals()))


def CreateReportDetail(request):

	if 'longitude' in request.POST :
		longitude = request.POST['longitude']
		full_time = request.POST['time']
		latitude = request.POST['latitude']
		monday = full_time.split('/')[1]+full_time.split('/')[2]
		time = full_time.split('/')[3]+full_time.split('/')[4]
		year = full_time.split('/')[0]
		checkID = request.POST['ID']
		r = ReportDetail (
				listptr = checkID, 
				longitude = longitude,
				 latitude = latitude,
				 time = time,
				 monday = monday,
				 year = year,
				 )
		r.save()

	else :
		checkID = request.POST['ID']
	
	cur_date = strftime("%d")
	cur_mon = strftime("%m")
	cur_year = strftime("%Y")

	monthlydata = Fetch(cur_mon, cur_date)

	return render_to_response('detail.html',RequestContext(request,locals()))


def Fetch(mon,day):

	start = (int(mon)-1)*100+int(day)
	end = int(mon)*100 + int(day)
	print start
	print end
	detail = ReportDetail.objects.filter(monday__gt=start)
	return detail
