from django.contrib import admin
from . import models

class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

class GroupAdmin(admin.ModelAdmin):
    inlines = [GroupMemberInline]

admin.site.register(models.Group, GroupAdmin)

