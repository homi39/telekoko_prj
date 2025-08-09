from django.contrib import admin
from .models import Group,User,Feeling


@admin.register(Group)
class EntryAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Feeling)
class UserAdmin(admin.ModelAdmin):
    pass
