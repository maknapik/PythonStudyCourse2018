from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import permission_required

app_name = 'manager'

urlpatterns = [
    # /home/
    url(r'^$', views.HomeView.as_view(), name='home'),

    # /home/register/
    url(r'^register/$', views.register_employee, name='register'),

    # /home/login/
    url(r'^login/$', views.login_employee, name='login'),

    # /home/login/
    url(r'^logout/$', views.logout_employee, name='logout'),

    # /groups/
    url(r'^groups/$', views.GroupsView.as_view(), name='groups'),

    # /employees/
    url(r'^employees/$', views.EmployeesView.as_view(), name='employees'),

    # /projects/
    url(r'^projects/$', views.ProjectsView.as_view(), name='projects'),

    # /groups/<pk>/
    url(r'^groups/(?P<pk>[0-9]+)/$', views.GroupView.as_view(), name='group'),

    # /employees/<pk>/
    url(r'^employees/(?P<pk>[0-9]+)/$', views.EmployeeView.as_view(), name='employee'),

    # /projects/<pk>/
    url(r'^projects/(?P<pk>[0-9]+)/$', views.ProjectView.as_view(), name='project'),

    # /groups/add
    url(r'^groups/add/$', views.CreateGroupView.as_view(), name='add_group'),

    # /groups/<pk>/update/
    url(r'^groups/(?P<pk>[0-9]+)/update/$', views.UpdateGroupView.as_view(), name='update_group'),

    # /groups/<pk>/delete/
    url(r'^groups/(?P<pk>[0-9]+)/delete/$', views.DeleteGroupView.as_view(), name='delete_group'),

    # /groups/<pk>/remove/<pk>/'
    url(r'^groups/(?P<group>[0-9]+)/(?P<pk>[0-9]+)/$', views.remove_employee, name='remove_employee'),

    # /employees/add
    url(r'^employees/add/$', views.add_employee, name='add_employee'),

    # /employees/<pk>/update/
    url(r'^employees/(?P<pk>[0-9]+)/update/$', views.UpdateEmployeeView.as_view(), name='update_employee'),

    # /employees/<pk>/delete/
    url(r'^employees/(?P<pk>[0-9]+)/delete/$', views.DeleteEmployeeView.as_view(), name='delete_employee'),

    # /projects/add
    url(r'^projects/add/$', views.CreateProjectView.as_view(), name='add_project'),

    # /projects/<pk>/update/
    url(r'^projects/(?P<pk>[0-9]+)/update/$', views.UpdateProjectView.as_view(), name='update_project'),

    # /projects/<pk>/delete/
    url(r'^projects/(?P<pk>[0-9]+)/delete/$', views.DeleteProjectView.as_view(), name='delete_project'),

    # /projects/<pk>/remove/<pk>/'
    url(r'^projects/(?P<project>[0-9]+)/(?P<pk>[0-9]+)/$', views.remove_employee_project, name='remove_employee_project')
]
