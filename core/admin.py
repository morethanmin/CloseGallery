from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Painting, Review_user, Review_celebrity, Main_event_slide,Weekly_painting

# Register your models here.

class Main_event_slideAdmin(admin.ModelAdmin):
  list_display = ['title','thumbnail_preview','type', 'comment']

  def thumbnail_preview(self, obj): 
    return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.thumbnail))

  thumbnail_preview.short_description = '썸네일'


class PaintingAdmin(admin.ModelAdmin):
  search_fields = ('title', 'text')
  list_display = ['title','thumbnail_preview', 'author']

  def thumbnail_preview(self, obj): 
    return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.thumbnail))

  thumbnail_preview.short_description = '썸네일'

admin.site.register(Painting, PaintingAdmin)
admin.site.register(Review_user)
admin.site.register(Review_celebrity)
admin.site.register(Main_event_slide,Main_event_slideAdmin)
admin.site.register(Weekly_painting)


