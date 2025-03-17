from django.urls import path
from .views import add_task
from .views import search_task
from .views import edit_task
from .views import delete_task

urlpatterns = [
    path('', search_task, name='search_task'),
    path('add_task/', add_task, name='add_task'),
    path(
        "edit_task/<int:task_id>/<int:page_number>/",edit_task, name="edit_task"),
    path("delete_task/<int:task_id>/<int:page_number>/", delete_task, name="delete_task"),
]
