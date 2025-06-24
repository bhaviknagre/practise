from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lawyer.urls')),
    path('', include('cases.urls')),
    path('', include('client.urls')),
    path('', include('document.urls')),
    path('', include('tasks.urls')),
]