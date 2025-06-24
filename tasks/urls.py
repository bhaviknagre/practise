from django.urls import path
from .views import (
    TaskListCreateAPIView, TaskDetailAPIView,
    TaskStatusListCreateAPIView, TaskStatusDetailAPIView,
    TaskPriorityListCreateAPIView, TaskPriorityDetailAPIView
)

urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),

    path('status/', TaskStatusListCreateAPIView.as_view(), name='task-status-list-create'),
    path('status/<int:pk>/', TaskStatusDetailAPIView.as_view(), name='task-status-detail'),

    path('priority/', TaskPriorityListCreateAPIView.as_view(), name='task-priority-list-create'),
    path('priority/<int:pk>/', TaskPriorityDetailAPIView.as_view(), name='task-priority-detail'),
]
