from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import TaskStatus, TaskPriority, Task
from .serializers import TaskStatusSerializer, TaskPrioritySerializer, TaskSerializer


class TaskListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.filter(assigned_to=request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Task, pk=pk)

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Task updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response({'message': 'Task deleted successfully'}, status=status.HTTP_204_NO_CONTENT)




class TaskStatusListCreateAPIView(APIView):
    def get(self, request):
        statuses = TaskStatus.objects.all()
        serializer = TaskStatusSerializer(statuses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskStatusDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(TaskStatus, pk=pk)

    def get(self, request, pk):
        serializer = TaskStatusSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        status_obj = self.get_object(pk)
        serializer = TaskStatusSerializer(status_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Task status updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TaskPriorityListCreateAPIView(APIView):
    def get(self, request):
        priorities = TaskPriority.objects.all()
        serializer = TaskPrioritySerializer(priorities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskPrioritySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskPriorityDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(TaskPriority, pk=pk)

    def get(self, request, pk):
        serializer = TaskPrioritySerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        priority = self.get_object(pk)
        serializer = TaskPrioritySerializer(priority, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Task priority updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
