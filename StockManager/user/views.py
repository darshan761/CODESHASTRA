from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import User, Stocks, Transaction
from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data

 
def getStocks(request):
	mydict = {'Microsoft':'MSFT','Google':'GOOG','Barclays':'BCS','JP Morgan Chase':'JPM','Bank of america':'bac'}
			#'Infosys':'infy','Tata Motors':'ttm','Berkshire':'berk','toyota':'tm','apple':'aapl',
			#'amazon':'amzn','Tesla':'tsla','Berkshire Hathaway':'brk.a','Facebook':'fb','Twitter':'twtr'}
	for i  in mydict.values():
		s = Stocks()
		param = {
		'q': "AAPL", # Stock symbol (ex: "AAPL")
        'i': "86400", # Interval size in seconds ("86400" = 1 day intervals)
        'x': "NASD", # Stock exchange symbol on which stock is traded (ex: "NASD")
        'p': "1M"
		}
		df = get_price_data(param)
		s.description = list(mydict.keys())[list(mydict.values()).index(i)]
		print(df)
	return render(request,'stockpage.html')


def login(request):
	return render(request,'login.html')

def enter(request):
	if User.objects.filter(username=request.POST.get('username'),password= request.POST.get('password')).exists():
				u = User.objects.get(username=request.POST['username'])
				request.session['usid'] = u.id
				context={'user':u}
				return render(request, 'home.html',context)
	else:
         e = "User doesn't exist"
	return render(request,'landingpage.html',{'error' : e})

def home(request):
	usr = User.objects.filter(id = request.session['usid'])
	for i in usr:
		u = i
	return render(request,'landingpage.html',{'u':u})

def stock(request):
	stock_list = Stocks.objects.all()
	return render(request,'stockpage.html',{'Stocks':stock_list})

def signup(request):
	return render(request,'signup.html')

def register(request):
	u = User()
	u.email = request.POST.get('email')
	u.name = request.POST.get('name')
	u.password = request.POST.get('password')
	u.mobile = request.POST.get('mobile')
	u.username = request.POST.get('username')
	error = ""
	if(u.password == request.POST.get('reppassword')):
		u.save()
		return render(request,'login.html')
	else:
		error = "Password didn't match" 

	return render(request,'signup.html',{"error":error})

def mystock(request):
	s = Stocks.objects.all()
	t = Transaction.objects.filter(user=request.session['usid'])
	us = []
	st  = []
	
	for j in t:
		us.append(j.stock)

	
	#print("jdygf",us)
	for i in s:
		if i.name in us:
			st.append(i)
	print("user",st)
	return render(request,'profile.html',{'st':us})


def profile(request):
	usr = User.objects.filter(id = request.session['usid'])
	for i in usr:
		u = i
	return render(request,'home.html',{'u':u})
	

def deleteStocks(request,slug):
	s = Stocks.objects.filter(id = slug)
	usr = User.objects.filter(id = request.session['usid'])
	for j in s:
		for i in usr:
			u = Transaction.objects.filter(user=i,stock = j)
			for j in u:
				loss = j.Val
				j.delete()

	usr = User.objects.filter(id = request.session['usid'])
	for i in usr:
		no = i.stock_no
		val = i.portfolio_val
	
	
	#Transaction.objects.filter(user=request.session['usid'],stock = slug).delete()
	usr.update(stock_no = no - 1,portfolio_val = val - loss)
	return render(request,'stockpage.html')

def addStocks(request,slug):
	s = Stocks.objects.filter(id = slug)
	s.update(quantity=int(request.POST.get('qts')))
	u = User.objects.filter(id=request.session['usid'])
	
	for i in u:
		uuu = i

	for i in s:
		sss = i
		cls = i.close
		#new.stock = slug
	
	#new.save()	
	if request.method == 'POST':
		
		v = cls * int(request.POST.get('qts'))
		u = User.objects.filter(id=request.session['usid'])
		for i in u:
			p = i.stock_no
			port = i.portfolio_val
			#p = i.stock
		#slug = p.append(slug)
		t = Transaction(stock=sss,user=uuu,quantity = int(request.POST.get('qts')),Val=v)
		t.save()
		u = User.objects.filter(id=request.session['usid']).update(stock_no = p+1,portfolio_val = port+v )

	return render(request,'stockpage.html')



def logout(request):
	return render(request,'login.html')

def about(request):
	return render(request,'about.html')

def know(request):
	return render(request,'jargons.html')

