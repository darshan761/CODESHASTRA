from django.urls import path

from . import views

urlpatterns = [
    path('user/', views.UserList.as_view()),
    path('user/create/' ,views.UserCreate.as_view()),
    path('user/delete/<int:pk>',views.UserDelete.as_view()),
    path('user/update/<int:pk>',views.UserUpdate.as_view()),
    path('user/<int:pk>', views.UserDetail.as_view()),
    path('stocks/', views.StockList.as_view()),
    path('stocks/create/' ,views.StockCreate.as_view()),
    path('stocks/delete/<int:pk>',views.StockDelete.as_view()),
    path('stocks/update/<int:pk>',views.StockUpdate.as_view()),
    path('stocks/<int:pk>', views.StockDetail.as_view()),
    
]