from django.contrib import admin

# Register your models here.
from polls.models import Poll, Choice, User
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class Usernline(admin.TabularInline):
    model = User
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    #date_hierarchy = 'pub_date'
    inlines = [ChoiceInline, Usernline]


admin.site.register(Poll, PollAdmin)

