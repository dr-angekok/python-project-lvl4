from django.urls import path
from tasks import views

urlpatterns = [
    path('statuses/', views.StatusesView.as_view(), name='statuses'),
    path('status/create/', views.StatusCreate.as_view(), name='status_create'),
    path('status/<int:pk>/update/', views.StatusUpdate.as_view(), name='status_update'),
    path('status/<int:pk>/delete/', views.StatusDelete.as_view(), name='status_delete'),
    path('status/<int:pk>/', views.StatusView.as_view(), name='status' ),
    path('tasks/', views.TasksView.as_view(), name='tasks'),
    path('tasks/<int:pk>/', views.TaskView.as_view(), name='task'),
    path('tasks/create/', views.TaskCreate.as_view(), name='task_create'),
    path('tasks/<int:pk>/update/', views.TaskUpdate.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', views.TaskDelete.as_view(), name='task_delete'),]
