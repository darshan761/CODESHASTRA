from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import User, Stocks ,Transaction

from .models import Stocks, User ,Transaction 
from .serializers import *  

class UserList(generics.ListAPIView):
	queryset = User.objects.filter()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.filter()
	serializer_class = UserSerializer


class UserCreate(generics.CreateAPIView):
	queryset = User.objects.filter()
	serializer_class = UserSerializer


class UserDelete(generics.DestroyAPIView):
    queryset = User.objects.filter()
    serializer_class = UserSerializer


class UserUpdate(generics.UpdateAPIView):
    queryset = User.objects.filter()
    serializer_class = UserSerializer


class StockList(generics.ListAPIView):
	queryset = Stocks.objects.filter()
	serializer_class = StockSerializer


class StockDetail(generics.RetrieveAPIView):
	queryset = Stocks.objects.filter()
	serializer_class = StockSerializer


class StockCreate(generics.CreateAPIView):
	queryset = Stocks.objects.filter()
	serializer_class = StockSerializer


class StockDelete(generics.DestroyAPIView):
    queryset = Stocks.objects.filter()
    serializer_class = StockSerializer


class StockUpdate(generics.UpdateAPIView):
    queryset = Stocks.objects.filter()
    serializer_class = StockSerializer
