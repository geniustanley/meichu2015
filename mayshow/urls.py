"""mayshow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home') Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from Main.views import *
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$',MainPageList),
	url(r'^list/',getReportList),
	url(r'^detail/(?P<ListId>[0-9]+)/$',CreateReportDetail),
	url(r'^new/',NewData),
	url(r'^addnew/(?P<ListId>[0-9]+)/',AddNew),
	url(r'^test',Test),
	url(r'^detail/(?P<ListId>[0-9]+)/gmap',GMap, name='gmap'),
	url(r'^detail/(?P<ListId>[0-9]+)/piechart',PieChart, name='piechart'),
	url(r'^detail/(?P<ListId>[0-9]+)/radar',Radar, name='radar'),
	url(r'^detail/(?P<ListId>[0-9]+)/linechart',LineChart, name='linechart'),
	url(r'^yearreport/(?P<ListId>[0-9]+)/',YearReport),
	url(r'^reporttime/(?P<ListId>[0-9]+)/',ReportTime),
]
