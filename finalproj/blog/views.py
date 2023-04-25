from django.shortcuts import render
from blog import models
import math

# Create your views here.

#blog頁面
# def blog(request):
#     return render(request, 'blog/apple-blog.html')

page1 = 1

def index(request, pageindex=None):  #首頁
	global page1
	pagesize = 3
	newsall = models.BlogPost.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1 = 1
		newsunits = models.BlogPost.objects.filter(enabled=True).order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1-2)*pagesize
		if start >= 0:
			newsunits = models.BlogPost.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
			page1 -= 1
	elif pageindex=='2':
		start = page1*pagesize
		if start < datasize:
			newsunits = models.BlogPost.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
			page1 += 1
	elif pageindex=='3':
		start = (page1-1)*pagesize
		newsunits = models.BlogPost.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
	currentpage = page1
	return render(request, "blog/apple-blog.html", locals())

def detail(request, detailid=None):  #詳細頁面
	unit = models.BlogPost.objects.get(id=detailid)
	category = unit.category
	title = unit.title
	pubtime = unit.publish_time
	tags = unit.tags
	content = unit.content
	unit.press += 1
	unit.save()
	return render(request, "blog/detail.html", locals())