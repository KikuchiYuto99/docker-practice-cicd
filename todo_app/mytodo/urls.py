from django.urls import path
from mytodo import views as mytodo
from .views import index, add, update_task_complete, delete_task, edit_task

urlpatterns = [
    path("", index, name="index"),
    path("add/", add, name="add"),
    path("update_task_complete/", update_task_complete, name="update_task_complete"),
    path("delete_task/<int:task_id>/", delete_task, name="delete_task"),
    path("edit_task/<int:task_id>/", edit_task, name="edit_task")
]
