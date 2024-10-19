from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Contact, Category, Team, Dish, Profile,Order, Students

admin.site.site_header = "MyComputers | Admin"

"""class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject','added_on','is_approved']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','added_on','updated_on']

class ClientAdmin(admin.ModelAdmin):
    list_display = ['id','name','added_on','updated_on']

class TeamAdmin(admin.ModelAdmin):
    list_display = ['id','name','added_on','updated_on']

class DishAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','added_on','updated_on']"""


admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Team )
admin.site.register(Dish)
admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(Students)