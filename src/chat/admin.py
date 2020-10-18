from django.contrib import admin

from .models import Contact, Chat, Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('contact', 'content', 'timestamp')

admin.site.register(Chat)
admin.site.register(Contact)
admin.site.register(Message, MessageAdmin)
