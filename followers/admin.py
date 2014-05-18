from django.contrib import admin
from django import forms

from followers.models import Man

thread_unsafe_follows_choices = ()
thread_unsafe_followed_by_choices = ()

class ManForm(forms.ModelForm):
    follows_choices = ((1,1),) # will be dynamically set from ManAdmin.get_form
    followed_by_choices = ((2,2),) # will be dynamically set from ManAdmin.get_form
    follows = forms.MultipleChoiceField(label='follows', choices=follows_choices)
    followed_by = forms.MultipleChoiceField(label='followed by', choices=followed_by_choices)

    class Meta:
        model = Man
        fields = ['name', 'follows', 'followed_by']

    def __init__(self, *args, **kwargs):
        super(ManForm, self).__init__(*args, **kwargs)
        self.fields['follows'] = forms.MultipleChoiceField(label='follows', choices=thread_unsafe_follows_choices)
        self.fields['followed_by'] = forms.MultipleChoiceField(label='followed by', choices=thread_unsafe_followed_by_choices)

class ManAdmin(admin.ModelAdmin):
    list_display = ('name', 'len_follows', 'len_followed_by')
    list_display_links = ('name',)
    form = ManForm

    def get_form(self, request, obj=None, **kwargs):
        '''
        This is an ugly hack, created for the following purpose:

        I want to customize the add/change page, by making it display 
        Multiselections with followers of currently selected Man. But
        I can't reach the currently selected Man from ManForm! 

        To overcome that, I recover Man's id from the request argument
        of this function and dynamically modify follows_choices and 
        followed_by_choices attributes of ManForm class. Yuck.

        TODO: Thread-safety!
        TODO: Exception handling!
        '''
        # get last component of path, it is Man id
        components = request.path.split("/")
        if len(components) > 1 and components[-1] == "":
            id = int(components[-2])
        elif len(components) > 0: 
            id = int(components[-1])
        man = Man.objects.get(id=id)

        # prepare 2-tuples in ManForm
        followers = self.follows(man)
        follows_choices = []
        for follower in followers:
            follows_choices.append((follower, follower))
        global thread_unsafe_follows_choices
        thread_unsafe_follows_choices = tuple(follows_choices)

        followed_by = self.followed_by(man)
        followed_by_choices = []
        for followed in followed_by:
            followed_by_choices.append((followed, followed))
        global thread_unsafe_followed_by_choices
        thread_unsafe_followed_by_choices = tuple(followed_by_choices)

        output_form = super(ManAdmin, self).get_form(request, obj, **kwargs)
        return output_form

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
