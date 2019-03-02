from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.login),
    path('login/' ,views.login,name = 'login'),
    path('signup/',views.signup,name = 'signup'),
    path('home/',views.home,name='home'),
    path('stock/',views.stock,name='stock'),
    path('about/',views.about,name='about'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logout,name='logout'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)