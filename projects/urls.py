from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
path('', views.projects, name='projects'),
path('add_project', views.add_project, name='add_project'),
path('projects/<int:project_id>/add_task/', views.add_task, name='add_task'),
path('projects/<int:project_id>/edit/', views.edit_project, name='edit_project'),
path('projects/<int:project_id>/delete/', views.delete_project, name='delete_project'),
path('projects/<int:project_id>/tasks/<int:task_id>/edit/', views.edit_task, name='edit_task'),
path('projects/<int:project_id>/tasks/<int:task_id>/delete/', views.delete_task, name='delete_task')
]