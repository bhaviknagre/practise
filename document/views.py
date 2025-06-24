from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import DocumentType, Document, Chunk, DocumentEntities
from .serializers import (
    DocumentTypeSerializer, DocumentSerializer,
    ChunkSerializer, DocumentEntitiesSerializer
)
from lawyer.models import LawyerProfile




class DocumentTypeListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        types = DocumentType.objects.all()
        serializer = DocumentTypeSerializer(types, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DocumentTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocumentTypeDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(DocumentType, pk=pk)

    def get(self, request, pk):
        serializer = DocumentTypeSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        obj = self.get_object(pk)
        serializer = DocumentTypeSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Document type updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class DocumentListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        documents = Document.objects.filter(uploaded_by__user=request.user)
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()
        try:
            data['uploaded_by'] = LawyerProfile.objects.get(user=request.user).id
        except LawyerProfile.DoesNotExist:
            return Response({'error': 'Lawyer profile not found.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = DocumentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocumentDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Document, pk=pk)

    def get(self, request, pk):
        serializer = DocumentSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        document = self.get_object(pk)
        data = request.data.copy()
        data.pop('uploaded_by', None)
        serializer = DocumentSerializer(document, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Document updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        document = self.get_object(pk)
        document.delete()
        return Response({'message': 'Document deleted successfully'}, status=status.HTTP_204_NO_CONTENT)




class ChunkListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, document_id):
        chunks = Chunk.objects.filter(document_id=document_id)
        serializer = ChunkSerializer(chunks, many=True)
        return Response(serializer.data)




class DocumentEntitiesListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, document_id):
        entities = DocumentEntities.objects.filter(document_id=document_id)
        serializer = DocumentEntitiesSerializer(entities, many=True)
        return Response(serializer.data)
