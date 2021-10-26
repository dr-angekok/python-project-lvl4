from django.urls import path
from tasks import views

urlpatterns = [
    path('statuses/', views.StatusesView.as_view(), name='statuses'),
    path('status/create/', views.StatusCreate.as_view(), name='status_create'),
    path('status/<int:pk>/update/', views.StatusUpdate.as_view(), name='status_update'),
    path('status/<int:pk>/delete/', views.StatusDelete.as_view(), name='status_delete'),
    path('status/<int:pk>/', views.StatusView.as_view(), name='status' ),]
