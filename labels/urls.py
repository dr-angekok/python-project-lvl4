from django.urls import path
from . import views

urlpatterns = [
    path('labels/', views.LabelsView.as_view(), name='labels'),
    path('labels/<int:pk>/', views.LabelView.as_view(), name='label'),
    path('labels/create/', views.LabelCreate.as_view(), name='label_create'),
    path('labels/<int:pk>/update/', views.LabelUpdate.as_view(), name='label_update'),
    path('labels/<int:pk>/delete/', views.LabelDelete.as_view(), name='label_delete')]