from django.db import models
from django.utils.html import mark_safe
from embed_video.fields import EmbedVideoField

# Gallery Category Model
class Gallery(models.Model):
	title=models.CharField(max_length=150)
	detail=models.TextField()
	img=models.ImageField(upload_to="gallery/",null=True)

	def __str__(self):
		return self.title

	def image_tag(self):
		return mark_safe('<img src="%s" width="80" />' % (self.img.url))


# Gallery Images Model
class GalleryImage(models.Model):
	gallery=models.ForeignKey(Gallery, on_delete=models.CASCADE,null=True)
	alt_text=models.CharField(max_length=150)
	img=models.ImageField(upload_to="gallery_imgs/",null=True)

	def __str__(self):
		return self.alt_text

	def image_tag(self):
		return mark_safe('<img src="%s" width="80" />' % (self.img.url))


# Youtube embedded video

class Item(models.Model):
    video_title = models.CharField(max_length=255, null=True, blank=True)
    video = EmbedVideoField()  # same like models.URLField()
    added_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_active = models.BooleanField(default=True,)


    def __str__(self):
        return self.video_title