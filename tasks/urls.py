from django.urls import path
from tasks import views

urlpatterns = [
    path('statuses/', views.StatusesView.as_view(), name='statuses'),
    path('statuses/create/', views.StatusCreate.as_view(), name='status_create'),
    path('statuses/<int:pk>/update/', views.StatusUpdate.as_view(), name='status_update'),
    path('statuses/<int:pk>/delete/', views.StatusDelete.as_view(), name='status_delete'),
    path('statuses/<int:pk>/', views.StatusView.as_view(), name='status'),
    path('tasks/', views.TasksView.as_view(), name='tasks'),
    path('tasks/<int:pk>/', views.TaskView.as_view(), name='task'),
    path('tasks/create/', views.TaskCreate.as_view(), name='task_create'),
    path('tasks/<int:pk>/update/', views.TaskUpdate.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', views.TaskDelete.as_view(), name='task_delete'),
    path('labels/', views.LabelsView.as_view(), name='labels'),
    path('labels/<int:pk>/', views.LabelView.as_view(), name='label'),
    path('labels/create/', views.LabelCreate.as_view(), name='label_create'),
    path('labels/<int:pk>/update/', views.LabelUpdate.as_view(), name='label_update'),
    path('labels/<int:pk>/delete/', views.LabelDelete.as_view(), name='label_delete')]
