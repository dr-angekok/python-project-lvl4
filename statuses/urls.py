from django.urls import path
from . import views

urlpatterns = [
    path('statuses/', views.StatusesView.as_view(), name='statuses'),
    path('statuses/create/', views.StatusCreate.as_view(), name='status_create'),
    path('statuses/<int:pk>/update/', views.StatusUpdate.as_view(), name='status_update'),
    path('statuses/<int:pk>/delete/', views.StatusDelete.as_view(), name='status_delete'),
    path('statuses/<int:pk>/', views.StatusView.as_view(), name='status')]
