from django import forms
from .models import Group
from .models import Employee
from django.contrib.auth.models import User

# adds new group
class GroupForm(forms.ModelForm):
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))

    class Meta:
        model = Group
        fields = ['name', 'description', 'photo']


# register new employee (user)
class UserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def save(self, employee_form):
        data = self.cleaned_data
        user = User(username=data['username'])
        user.set_password(data['password'])
        user.save()
        employee_data = employee_form.cleaned_data
        employee = Employee(name=employee_data['name'], surname=employee_data['surname'], user=user)
        employee.save()
        return user


# login employee
class EmployeeLoginForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    surname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Surname'}))

    def save(self, commit=True):
        data = self.cleaned_data
        employee = Employee(name=data['name'], surname=data['surname'])
        if commit:
            employee.save()
        return employee


# login user
class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def save(self, commit=True):
        data = self.cleaned_data
        user = User(username=data['username'], password=data['password'])
        if commit:
            user.save()
        return user

