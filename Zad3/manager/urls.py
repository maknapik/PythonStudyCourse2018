from django.conf.urls import url
from . import views

app_name = 'manager'

urlpatterns = [
    # /home/
    url(r'^$', views.HomeView.as_view(), name='home'),

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
    url(r'^groups/(?P<pk>[0-9]+)/delete/$', views.UpdateGroupView.as_view(), name='update_group'),

    # /groups/<pk>/delete/
    url(r'^groups/(?P<pk>[0-9]+)/delete/$', views.DeleteGroupView.as_view(), name='delete_group'),
]
