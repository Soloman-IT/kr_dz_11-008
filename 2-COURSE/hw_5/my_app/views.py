from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

count = 0

def main(request):
	template = loader.get_template("my_app/main.html")
	global count
	count += 1
	context = {"count" : count}
	return HttpResponse(template.render(context,request))

count_1 = 0

def news(request):
	template = loader.get_template("my_app/news.html")
	global count_1
	count_1 += 1
	context = {"count" : count_1}
	return HttpResponse(template.render(context,request))

count_2 = 0

def profile(request):
	template = loader.get_template("my_app/profile.html")
	global count_2
	count_2 += 1
	context = {"count" : count_2}
	return HttpResponse(template.render(context,request))