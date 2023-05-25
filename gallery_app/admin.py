from django.contrib import admin
from .models import Gallery, GalleryImage
from  embed_video.admin  import  AdminVideoMixin
from .models import Item

# Register your models here.

class GalleryAdmin(admin.ModelAdmin):
	list_display=('title','image_tag')

admin.site.register(Gallery,GalleryAdmin)


class GalleryImageAdmin(admin.ModelAdmin):
	list_display=('alt_text','image_tag')
	
admin.site.register(GalleryImage,GalleryImageAdmin)



# Register youtube models here.

class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('video_title','added_at','is_active')
    list_editable = ('is_active',)
    list_filter = ('video_title',)

admin.site.register(Item, VideoAdmin)