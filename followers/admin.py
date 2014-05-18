from django.contrib import admin
from django import forms

from followers.models import Man, Follow

class FollowsInline(admin.TabularInline):
    model = Follow
    fk_name = "who"
    verbose_name = "followed by this Man"
    verbose_name_plural = "Follows"

class FollowedInline(admin.TabularInline):
    model = Follow
    fk_name = "whom"
    verbose_name = "following this Man"
    verbose_name_plural = "Followed by"

class ManAdmin(admin.ModelAdmin):
    list_display = ('name', 'len_follows', 'len_followed_by')
    list_display_links = ('name',)
    inlines = [FollowsInline, FollowedInline]

    def follows(self, obj):
        '''returns list of Men, whom obj follows'''
        return Follow.objects.filter(who=obj)

    def len_follows(self, obj):
        return str(len(self.follows(obj)))

    def followed_by(self, obj):
        '''returns list of Men, who follow obj'''
        return Follow.objects.filter(whom=obj)

    def len_followed_by(self, obj):
        return str(len(self.followed_by(obj)))

admin.site.register(Man, ManAdmin)
