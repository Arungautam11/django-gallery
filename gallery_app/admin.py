from django.contrib import admin
from .models import Gallery, GalleryImage

# Register your models here.

class GalleryAdmin(admin.ModelAdmin):
	list_display=('title','image_tag')

admin.site.register(Gallery,GalleryAdmin)


class GalleryImageAdmin(admin.ModelAdmin):
	list_display=('alt_text','image_tag')
	
admin.site.register(GalleryImage,GalleryImageAdmin)