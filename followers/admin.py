from django.contrib import admin
from django import forms

from followers.models import Man, Follows

class FollowsInline(admin.TabularInline):
    model = Follows
    fk_name = "who"

class FollowedInline(admin.TabularInline):
    model = Follows
    fk_name = "whom"

class ManAdmin(admin.ModelAdmin):
    list_display = ('name', 'len_follows', 'len_followed_by')
    list_display_links = ('name',)
    inlines = [FollowsInline, FollowedInline]

    def follows(self, obj):
        '''returns list of Men, whom obj follows'''
        return obj.follow_ids.split(" ")

    def len_follows(self, obj):
        return str(len(self.follows(obj)))

    def followed_by(self, obj):
        '''returns list of Men, who follow obj'''
        output = []
        for follower in Man.objects.all():
            all_followed = str(follower.follow_ids).split(" ")
            for followed in all_followed:
                if followed and int(followed) == int(obj.id): 
                    output.append(unicode(follower.id))
                    break
        return output

    def len_followed_by(self, obj):
        return str(len(self.followed_by(obj)))

admin.site.register(Man, ManAdmin)
