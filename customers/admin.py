from django.contrib import admin
from .models import TourRegistration

# admin.site.register(Tour)
admin.site.register(TourRegistration)
# admin.site.register(Image)

# class ImageAdmin(admin.StackedInline):
#     model = Image
#
# @admin.register(Tour)
# class TourAdmin(admin.ModelAdmin):
#     inlines = [ImageAdmin]
#
#     class Meta:
#         model=Tour
#
# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     pass