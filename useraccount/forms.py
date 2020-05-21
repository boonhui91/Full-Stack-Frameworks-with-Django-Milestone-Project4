from django import forms
from .models import Profile
from django.contrib.auth.models import Group



user_type= [
    ('customer', 'Customer'),
    ('vendor', 'Vendor')
    ]

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    # create radio buttons for selection
    user_status = forms.CharField(widget=forms.RadioSelect(choices=user_type))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        # save profile
        profile = Profile()
        user.save()
        profile.user = user
        profile.save()

        # if user create as vendor account
        if self.cleaned_data['user_status'] == 'vendor':
            # assign user vendor group
            user_group = Group.objects.get(name='vendor')
            user_group.user_set.add(user)

        # if user create as customer account
        else:
            # assign user customer group
            user_group = Group.objects.get(name='customer')
            user_group.user_set.add(user)