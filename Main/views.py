from django.shortcuts import render_to_response
from Main.models import ReportList
from Main.models import ReportDetail
from django.template import RequestContext

# Create your views here.


def MainPageList(request):	

	RList = ReportList.objects.all()
	return render_to_response('index.html',RequestContext(request,locals()))


def CreateReportDetail(request):

	if 'longtitude' in request.POST :
		longtitude = request.POST['longtitude']
		time = request.POST['time']
		latitude = request.POST['latitude']
		checkID = request.POST['ID']
		r = ReportDetail (
				listptr = checkID, 
				longtitude = longtitude,
				 latitude = latitude,
				 time = time,
				 )
		r.save()

	else :
		checkID = request.POST['RID']


	return render_to_response('detail.html',RequestContext(request,locals()))


