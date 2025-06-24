from django.db import models
from lawyer.models import LawyerProfile


class DocumentType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Document Type"
        verbose_name_plural = "Document Types"
        ordering = ['name']


class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    document_type = models.ForeignKey(DocumentType, on_delete=models.SET_NULL, null=True, blank=True, related_name='documents')
    case = models.ForeignKey('cases.Case', on_delete=models.CASCADE, related_name='documents')
    uploaded_by = models.ForeignKey(LawyerProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='uploaded_documents')
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    file_type = models.CharField(max_length=20, blank=True, null=True)
    file_size_kb = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.file:
            if not self.file_type:
                self.file_type = self.file.name.split('.')[-1].lower()
            if not self.file_size_kb:
                self.file_size_kb = int(self.file.size / 1024)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = "Document"
        verbose_name_plural = "Documents"


class Chunk(models.Model):
    text = models.TextField()
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='chunks')

    def __str__(self):
        preview = self.text.strip().replace('\n', ' ')[:50]
        return f"Chunk {self.id} - {preview}..."

    class Meta:
        ordering = ['id']
        verbose_name = "Document Chunk"
        verbose_name_plural = "Document Chunks"


class DocumentEntities(models.Model):
    attribute = models.CharField(max_length=255)
    value = models.TextField()
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='entities')
    chunk = models.ForeignKey(Chunk, on_delete=models.CASCADE, related_name='entities')

    def __str__(self):
        preview = self.value.strip().replace('\n', ' ')[:50]
        return f"{self.attribute}: {preview}..."

    class Meta:
        ordering = ['id']
        verbose_name = "Document Entity"
        verbose_name_plural = "Document Entities"
