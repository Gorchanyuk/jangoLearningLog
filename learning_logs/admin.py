from django.contrib import admin

# Register your models here.
from learning_logs.models import Topic, Entry, Pizza, Topping



class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'date_added', 'owner')
    list_display_links = ('id', 'text',)
    search_fields = ('owner', 'text')
    list_filter = ('date_added', 'owner')

class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'text', 'date_added',)
    list_display_links = ('id', 'text')
    search_fields = ('topic', 'text')
    list_filter = ('date_added', 'topic')

admin.site.register(Topic, TopicAdmin)
admin.site.register(Entry, EntryAdmin)
