from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, redirect
from Main.models import ReportList
from Main.models import ReportDetail
from django.template import RequestContext
from time import strftime
from django.forms.models import model_to_dict
import datetime
# Create your views here.

def getReportList(request):
	result = []
	for report in ReportList.objects.all():
		result.append({'id': report.id, 'name': report.reportname})
	return JsonResponse({"list": result})


def MainPageList(request):	
	
	RList = ReportList.objects.all()
	return render_to_response('index.html',RequestContext(request,locals()))


def CreateReportDetail(request,ListId):
	result = []
	checkID = ListId
	
	cur_date = strftime("%d")
	cur_mon = strftime("%m")
	cur_year = strftime("%Y")

	monthlydata = Fetch(cur_mon, cur_date, checkID)

	for data in monthlydata :
		result.append({'longitude':data.longitude, 'latitude':data.latitude,'time':data.time,'age':int(cur_year)-data.bornyear})
	return JsonResponse({"result":result})
	#return render_to_response('gmap.html',RequestContext(request,locals()))

@csrf_exempt
def NewData(request):
		bornyear = int(request.POST['bornyear'])
		longitude = request.POST['longitude']
		full_time = request.POST['time']
		latitude = request.POST['latitude']
		year = int(full_time.split('/')[0])
		month = int(full_time.split('/')[1])
		day = int(full_time.split('/')[2])
		hour = int(full_time.split('/')[3])
		minute = int(full_time.split('/')[4])
		checkID = request.POST['ID']
		time = datetime.datetime(year, month, day, hour, minute)
		r = ReportDetail (
				 listptr = checkID, 
				 longitude = longitude,
				 latitude = latitude,
				 time = time,
				 bornyear = bornyear,
				 )
		r.save()

		return redirect('/detail/%s' % checkID)

def ReportTime(request, ListId):
	result = []
	dayBefore = request.GET.get('day')

	if dayBefore == None:
		reports = ReportDetail.objects.filter(listptr=ListId)
		print len(reports)
	else:
		time = datetime.datetime.now() - datetime.timedelta(days=int(dayBefore))
		reports = ReportDetail.objects.filter(listptr=ListId).filter(time__gte=time)
		print len(reports)
	result = [0, 0, 0, 0, 0, 0]
	for report in reports:
		print report.time.hour
		if report.time.hour != 0:
			result[report.time.hour / 4] += 1
	return JsonResponse({'result': result})

def Fetch(mon,day,checkid):
	now = datetime.datetime.now()
	time = now - datetime.timedelta(days=30)
	print time
	return ReportDetail.objects.filter(listptr=checkid).filter(time__gte=time)

def YearReport(request, ListId):
	result = []
	year = int(request.GET.get('year'))
	month = int(request.GET.get('month'))
	reports = ReportDetail.objects.filter(listptr=ListId)

	# check valid input

	if ( month < 0 or month > 12): month = 0

	cur_year =int( strftime("%Y") )
	
	if ( month == 0 ):

		time = datetime.datetime(year,1,1)
		time_next = datetime.datetime(year+1,1,1)
		reports = reports.filter(time__gte=time).filter(time__lt = time_next)
	else :
		time = datetime.datetime(year,month,1)
		if ( month != 12):
			time_next = datetime.datetime(year,month+1,1)
			reports = reports.filter(time__gte=time).filter(time__lt=time_next)
		else :
			
			reports = reports.filter(time__gte=time)
			
	for i in range(0,14):
		cnt = 0
		for j in range(4):
			age = cur_year - i *5 +j
			cnt += reports.filter(bornyear = age).count()
		result.append(cnt)
	cnt = 0
	cnt = reports.filter(bornyear__lt =  (cur_year - 70)  ).count()
	result.append(cnt)
	return JsonResponse({'result':result})


def Radar(request, ListId):
	reportId = ListId
	return render_to_response('radar.html',RequestContext(request,locals()))

def PieChart(request, ListId):
	reportId = ListId
	return render_to_response('piechart.html',RequestContext(request,locals()))

def LineChart(request,ListId):
	reportId = ListId
	return render_to_response('linechart.html',RequestContext(request,locals()))

def GMap(request, ListId):
	reportId = ListId
	return render_to_response('gmap.html',RequestContext(request,locals()))

def Test(request):
	return render_to_response('test.html',RequestContext(request,locals()))

def AddNew(request,ListId):
	checkID = ListId
	return render_to_response('addnew.html',RequestContext(request,locals()))
