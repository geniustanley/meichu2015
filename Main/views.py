from django.shortcuts import render_to_response
from Main.models import ReportList
from Main.models import ReportDetail
from django.template import RequestContext

# Create your views here.


def MainPageList(request):
	RList = ReportList.objects.all()

	return render_to_response('index.html',RequestContext(request,locals()))


def CreateReportDetail():
	
	return render_to_response('',RequestContext(request,locals()))


