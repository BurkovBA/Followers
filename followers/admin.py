from django.contrib import admin
# Register your models here.

from followers.models import ManMan

class ManAdmin(admin.ModelAdmin):
    list_display = ('name', 'follows', 'followed_by')
    list_display_links = ('name',)

    def follows(self, obj):
        return len(obj.follow_ids.split(" "))

    def followed_by(self, obj):
        counter = 0
        for man in ManMan.objects.all():
            followed = str(man.follow_ids).split(" ")
            for celebrity in followed:
                if celebrity and int(celebrity) == int(obj.id): counter += 1
        return str(counter)

admin.site.register(ManMan, ManAdmin)
