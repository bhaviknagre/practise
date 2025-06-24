from django.urls import path
from .views import (
    DocumentTypeListCreateAPIView, DocumentTypeDetailAPIView,
    DocumentListCreateAPIView, DocumentDetailAPIView,
    ChunkListAPIView, DocumentEntitiesListAPIView
)

urlpatterns = [

    path('types/', DocumentTypeListCreateAPIView.as_view(), name='document-type-list-create'),
    path('types/<int:pk>/', DocumentTypeDetailAPIView.as_view(), name='document-type-detail'),

    path('documents/', DocumentListCreateAPIView.as_view(), name='document-list-create'),
    path('documents/<int:pk>/', DocumentDetailAPIView.as_view(), name='document-detail'),

    path('documents/<int:document_id>/chunks/', ChunkListAPIView.as_view(), name='chunk-list'),
    path('documents/<int:document_id>/entities/', DocumentEntitiesListAPIView.as_view(), name='entity-list'),
]
