from rest_framework import serializers
from .models import DocumentType, Document, Chunk, DocumentEntities


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
        read_only_fields = ['uploaded_by', 'uploaded_at', 'updated_at', 'file_type', 'file_size_kb']


class ChunkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chunk
        fields = '__all__'


class DocumentEntitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentEntities
        fields = '__all__'
