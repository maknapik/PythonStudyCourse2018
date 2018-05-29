from django.contrib.auth.models import User
from django import forms
from .models import Group


class GroupForm(forms.ModelForm):
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))

    class Meta:
        model = Group
        fields = ['name', 'description', 'photo']