from django.contrib import admin
from .models import Room,Topic,Message
# Register your models here.

# class RoomAdmin(admin.ModelAdmin):
#     list_display = ['name','updated']
#     search_fields = ('created',)
    
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)