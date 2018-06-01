from django.views import generic
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Group, Employee, Project
from .forms import GroupForm


class HomeView(generic.TemplateView):
    template_name = 'manager/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['group_count'] = Group.objects.count()
        context['employee_count'] = Employee.objects.count()
        context['project_count'] = Project.objects.count()
        return context


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


class CreateGroupView(generic.CreateView):
    model = Group
    form_class = GroupForm


class UpdateGroupView(generic.UpdateView):
    model = Group
    form_class = GroupForm


class DeleteGroupView(generic.DeleteView):
    model = Group
    success_url = reverse_lazy('manager:groups')


def remove_employee(request, group, pk):
    Employee.objects.filter(pk=pk).update(group=None)
    return redirect('manager:group', pk=group)


class CreateEmployeeView(generic.CreateView):
    model = Employee
    fields = ['name', 'surname', 'salary', 'group', 'projects']


class UpdateEmployeeView(generic.UpdateView):
    model = Employee
    fields = ['name', 'surname', 'salary', 'group', 'projects']


class DeleteEmployeeView(generic.DeleteView):
    model = Employee
    success_url = reverse_lazy('manager:employees')


class CreateProjectView(generic.CreateView):
    model = Project
    fields = ['name', 'description', 'budget']


class UpdateProjectView(generic.UpdateView):
    model = Project
    fields = ['name', 'description', 'budget']


class DeleteProjectView(generic.DeleteView):
    model = Project
    success_url = reverse_lazy('manager:projects')


def remove_employee_project(request, project, pk):
    p = Project.objects.get(pk=project)
    e = Employee.objects.get(pk=pk)
    e.projects.remove(p)
    return redirect('manager:project', pk=project)


def remove_project(request, employee, pk):
    p = Project.objects.get(pk=pk)
    e = Employee.objects.get(pk=employee)
    e.projects.remove(p)
    return redirect('manager:employee', pk=employee)
