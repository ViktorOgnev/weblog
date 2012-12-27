from django.contrib import admin
from cab.models import Language, Snippet, Bookmark

class LanguageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}

class SnippetAdmin(admin.ModelAdmin):
   pass
   
class BookmarkAdmin(admin.ModelAdmin):
   pass
    
admin.site.register(Language, LanguageAdmin)
admin.site.register(Snippet, SnippetAdmin)
admin.site.register(Bookmark, BookmarkAdmin)

