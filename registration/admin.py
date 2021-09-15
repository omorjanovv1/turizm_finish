from django.contrib import admin
from .models import User
from customers.models import Tour
from customers.models import TourRegistration


# Register your models here.

class ProductInline(admin.TabularInline):
    model = TourRegistration


class Project(admin.ModelAdmin):
    model = User
    inlines = [ProductInline, ]


admin.site.register(User, Project)


class Project(admin.ModelAdmin):
    model = Tour
    inlines = [ProductInline, ]


admin.site.register(Tour, Project)
