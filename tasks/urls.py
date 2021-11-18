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
    path('lables/', views.LablesView.as_view(), name='lables'),
    path('lables/<int:pk>/', views.LableView.as_view(), name='lable'),
    path('lables/create/', views.LableCreate.as_view(), name='lable_create'),
    path('lables/<int:pk>/update/', views.LableUpdate.as_view(), name='lable_update'),
    path('lables/<int:pk>/delete/', views.LableDelete.as_view(), name='lable_delete')]
