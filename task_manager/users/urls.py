from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("", views.List.as_view(), name="list"),
    path("create/", views.Create.as_view(), name="create"),
    path("<int:pk>/update/", views.Update.as_view(), name="update"),
    path("<int:pk>/delete/", views.Delete.as_view(), name="delete"),
]
