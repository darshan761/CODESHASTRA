from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import User, Stocks

 
def login(request):
	return render(request,'login.html')

def home(request):
	return render(request,'home.html')

def stock(request):
	return render(request,'stockpage.html')

def signup(request):
	return render(request,'signup.html')

def profile(request):
	return render(request,'profile.html')

def addStocks(request):
	return render(request,'stockpage.html')

def deleteStocks(request):
	return render(request,'stockpage.html')

def logout(request):
	return render(request,'login.html')

def about(request):
	return render(request,'about.html')

