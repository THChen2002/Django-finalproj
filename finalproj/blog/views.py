from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from blog import models
import math
from datetime import datetime, timedelta
from django.utils import timezone
from accounts.models import UserProfile
import urllib.parse
# Create your views here.

#blog頁面
# def blog(request):
#     return render(request, 'blog/apple-blog.html')

page1 = 1

def index(request, pageindex=None, category="all"):  #首頁
	q = request.GET.get('q', None)
	newsall  = ''
	if category != "all":
		if q == None or q == "":
			newsall = models.BlogPost.objects.filter(category=models.Category.objects.get(title=category)).order_by('-id')
		elif q !=  None:
			newsall = models.BlogPost.objects.filter(title__contains=q)
	else:
		if q == None or q == "":
			newsall = models.BlogPost.objects.all().order_by('-id')
		elif q !=  None:
			newsall = models.BlogPost.objects.filter(title__contains=q)
	global page1
	pagesize = 3
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if q == None or q == "":
		if pageindex==None:
			page1 = 1
			newsunits = newsall.filter(enabled=True).order_by('-id')[:pagesize]
		elif pageindex=='1':
			start = (page1-2)*pagesize
			if start >= 0:
				newsunits = newsall.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
				page1 -= 1
		elif pageindex=='2':
			start = page1*pagesize
			if start < datasize:
				newsunits = newsall.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
				page1 += 1
		elif pageindex=='3':
			start = (page1-1)*pagesize
			newsunits = newsall.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
	elif q !=  None:
		if pageindex==None:
			page1 = 1
			newsunits = newsall.filter(enabled=True, title__contains=q).order_by('-id')[:pagesize]
		elif pageindex=='1':
			start = (page1-2)*pagesize
			if start >= 0:
				newsunits = newsall.filter(enabled=True, title__contains=q).order_by('-id')[start:(start+pagesize)]
				page1 -= 1
		elif pageindex=='2':
			start = page1*pagesize
			if start < datasize:
				newsunits = newsall.filter(enabled=True, title__contains=q).order_by('-id')[start:(start+pagesize)]
				page1 += 1
		elif pageindex=='3':
			start = (page1-1)*pagesize
			newsunits = newsall.filter(enabled=True, title__contains=q).order_by('-id')[start:(start+pagesize)]
	currentpage = page1

	return render(request, "blog/blogindex.html", locals())

def detail(request, category=None, id=None):  #詳細頁面
	if request.method == 'POST':
		bcontent = request.POST.get('bcontent')
		bblogpost = models.BlogPost.objects.get(id=request.POST.get('bblogpost'))
		bauthor = UserProfile.objects.get(id=request.POST.get('bauthor'))
		board = models.BoardUnit.objects.create(bblogpost=bblogpost, bcontent=bcontent, bauthor=bauthor)
		board.save()
		return redirect(reverse('blog_detail', args=[id]))
	else:
		unit = get_object_or_404(models.BlogPost, id=id)
		category = unit.category
		title = unit.title
		pubtime = unit.publish_time
		tags = unit.tags
		content = unit.content
		unit.press += 1
		unit.save()
		boards = models.BoardUnit.objects.filter(bblogpost=unit)
		now = timezone.now()
		for board in boards:
			timedelta = now - board.btime
			minutes = int(timedelta.seconds / 60)
			board.btimedelta = minutes
			board.save()
	return render(request, "blog/detail.html", locals())