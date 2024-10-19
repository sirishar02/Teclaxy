"""
URL configuration for teclaxy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tapp import views 
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('clients/',views.team_members,name="team"),
    path('Courses/',views.all_dishes,name="all_dishes"),
    path('register/',views.register,name="register"),
    path('check_user_exists/',views.check_user_exists,name="check_user_exist"),
    path('login/', views.signin, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    #path('dish/<int:id>/', views.single_dish, name='dish'),
    path('dish/<int:id>/', views.dish_detail, name='dish'),
    #path('paypal/',include('paypal.standard.ipn.urls')),
    #path('payment_done/', views.payment_done, name='payment_done'),
    #path('payment_cancel/', views.payment_cancel, name='payment_cancel'),
    path('registration/', views.registration, name='registration'),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
