from django.views import generic
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Group, Employee, Project
from .forms import GroupForm, UserForm, EmployeeLoginForm, UserLoginForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout


# home view
class HomeView(generic.TemplateView):
    template_name = 'manager/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['group_count'] = Group.objects.count()
        context['employee_count'] = Employee.objects.count() - 1
        context['project_count'] = Project.objects.count()
        context['groups'] = Group.objects.all()
        context['employees'] = Employee.objects.all()
        context['projects'] = Project.objects.all()
        return context


# standard views
class GroupsView(generic.ListView):
    template_name = 'manager/groups.html'
    model = Group
    context_object_name = 'groups'


class EmployeesView(generic.ListView):
    template_name = 'manager/employees.html'
    model = Employee
    context_object_name = 'employees'


class ProjectsView(generic.ListView):
    template_name = 'manager/projects.html'
    model = Project
    context_object_name = 'projects'


# views of certain model
class GroupView(generic.TemplateView):
    template_name = 'manager/group.html'

    def get_context_data(self, **kwargs):
        context = super(GroupView, self).get_context_data(**kwargs)
        context['group'] = Group.objects.get(pk=self.kwargs['pk'])
        context['employees'] = Employee.objects.filter(group=context['group'])
        return context


class EmployeeView(generic.TemplateView):
    template_name = 'manager/employee.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(pk=self.kwargs['pk'])
        context['projects'] = context['employee'].projects.all()
        return context


class ProjectView(generic.TemplateView):
    template_name = 'manager/project.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        context['project'] = Project.objects.get(pk=self.kwargs['pk'])
        context['employees'] = context['project'].employee_set.all()
        return context


# group managing views
class CreateGroupView(generic.CreateView):
    model = Group
    form_class = GroupForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('manager:groups')
        else:
            return super(CreateGroupView, self).dispatch(request, *args, **kwargs)


class UpdateGroupView(generic.UpdateView):
    model = Group
    form_class = GroupForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('manager:groups')
        return super(UpdateGroupView, self).dispatch(request, *args, **kwargs)


class DeleteGroupView(generic.DeleteView):
    model = Group
    success_url = reverse_lazy('manager:groups')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('manager:groups')
        return super(DeleteGroupView, self).dispatch(request, *args, **kwargs)


def remove_employee(request, group, pk):
    if not request.user.is_superuser:
        return redirect('manager:group', pk=group)
    else:
        Employee.objects.filter(pk=pk).update(group=None)
        return redirect('manager:group', pk=group)


# employee managing views
def add_employee(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        employee_form = EmployeeLoginForm(request.POST)
        if user_form.is_valid() and employee_form.is_valid():
            user_form.save(employee_form=employee_form)
            return redirect('manager:home')
        else:
            pass
    else:
        if not request.user.is_superuser:
            return redirect('manager:home')
        user_form = UserForm(request.POST)
        employee_form = EmployeeLoginForm(request.POST)
        return render(request, 'manager/registration_form.html', {
            'user_form': user_form,
            'employee_form': employee_form})


class UpdateEmployeeView(generic.UpdateView):
    model = Employee
    fields = ['name', 'surname', 'salary', 'photo', 'group', 'projects']

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser and not request.user.id == int(kwargs.get('pk')):
            return redirect('manager:employees')
        return super(UpdateEmployeeView, self).dispatch(request, *args, **kwargs)


class DeleteEmployeeView(generic.DeleteView):
    model = Employee
    success_url = reverse_lazy('manager:employees')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('manager:employees')
        return super(DeleteEmployeeView, self).dispatch(request, *args, **kwargs)


# project managing views
class CreateProjectView(generic.CreateView):
    model = Project
    fields = ['name', 'description', 'budget']

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('manager:projects')
        return super(CreateProjectView, self).dispatch(request, *args, **kwargs)


class UpdateProjectView(generic.UpdateView):
    model = Project
    fields = ['name', 'description', 'budget']

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('manager:project')
        return super(UpdateProjectView, self).dispatch(request, *args, **kwargs)


class DeleteProjectView(generic.DeleteView):
    model = Project
    success_url = reverse_lazy('manager:projects')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('manager:projects')
        return super(DeleteProjectView, self).dispatch(request, *args, **kwargs)


# remove employee from project page or project from employee page
def remove_employee_project(request, pk, project):
    if not request.user.is_superuser and not request.user.id == int(pk):
        if 'projects' in request.META.get('HTTP_REFERER'):
            return redirect('manager:project', project)
        else:
            return redirect('manager:employee', pk)
    else:
        p = Project.objects.get(pk=project)
        e = Employee.objects.get(pk=pk)
        e.projects.remove(p)
        if 'projects' in request.META.get('HTTP_REFERER'):
            return redirect('manager:project', project)
        else:
            return redirect('manager:employee', pk)


# register view
def register_employee(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        employee_form = EmployeeLoginForm(request.POST)
        if user_form.is_valid() and employee_form.is_valid():
            user_form.save(employee_form=employee_form)
            return redirect('manager:home')
        else:
            pass
    else:
        if request.user.is_authenticated:
            return redirect('manager:home')
        user_form = UserForm(request.POST)
        employee_form = EmployeeLoginForm(request.POST)
        return render(request, 'manager/registration_form.html', {
            'user_form': user_form,
            'employee_form': employee_form})


# login view
def login_employee(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('manager:home')
            else:
                form = UserLoginForm(request.POST)
                return render(request, 'manager/employee_form.html', {'form': form})
    else:
        if request.user.is_authenticated:
            return redirect('manager:home')
        form = UserLoginForm(request.POST)
        return render(request, 'manager/employee_form.html', {'form': form})


# logout view
def logout_employee(request):
    logout(request)
    return redirect('manager:login')

