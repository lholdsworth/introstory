from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User

# class ProfileInline(admin.TabularInline):
# 	model = User

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('display_name','account_type','user',)

admin.site.register(Profile, ProfileAdmin)