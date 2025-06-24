# Document API

API endpoints for managing legal documents and related operations.

## Endpoints

### 1. List Documents
- **URL**: `/api/documents/`
- **Method**: GET
- **Authentication**: Required
- **Description**: Get a list of all documents
- **Query Parameters**:
  - `search`: Search by title
  - `document_type`: Filter by document type
  - `case`: Filter by case ID
  - `uploaded_by`: Filter by uploader ID
  - `file_type`: Filter by file type
  - `ordering`: Order by field (e.g., `-uploaded_at`)
- **Response**:
  ```json
  {
    "count": 10,
    "next": "http://api.example.com/api/documents/?page=2",
    "previous": null,
    "results": [
      {
        "id": 1,
        "title": "Evidence Document",
        "document_type": "Evidence",
        "case": {
          "id": 1,
          "title": "Smith vs. State"
        },
        "uploaded_by": {
          "id": 1,
          "name": "John Doe"
        },
        "uploaded_at": "2025-01-15T10:30:00Z",
        "file_type": "pdf",
        "file_size_kb": 1024
      }
    ]
  }
  ```

### 2. Upload Document
- **URL**: `/api/documents/`
- **Method**: POST
- **Authentication**: Required
- **Description**: Upload a new document
- **Request Body**: Multipart form data
  ```json
  {
    "title": "Evidence Document",
    "document_type": 1,
    "case": 1,
    "description": "Important evidence for the case",
    "file": [binary file data]
  }
  ```
- **Response**: Created document object

### 3. Get Document Details
- **URL**: `/api/documents/{id}/`
- **Method**: GET
- **Authentication**: Required
- **Description**: Get details of a specific document
- **Response**: Document object with full details

### 4. Update Document
- **URL**: `/api/documents/{id}/`
- **Method**: PUT/PATCH
- **Authentication**: Required
- **Description**: Update document information
- **Request Body**: Same as Create with optional fields
- **Response**: Updated document object

### 5. Delete Document
- **URL**: `/api/documents/{id}/`
- **Method**: DELETE
- **Authentication**: Required
- **Description**: Delete a document

### 6. Download Document
- **URL**: `/api/documents/{id}/download/`
- **Method**: GET
- **Authentication**: Required
- **Description**: Download the document file
- **Response**: File download stream

### 7. Document Types
- **URL**: `/api/documents/types/`
- **Method**: GET
- **Authentication**: Required
- **Description**: Get list of available document types
- **Response**:
  ```json
  {
    "types": [
      {
        "id": 1,
        "name": "Evidence"
      },
      {
        "id": 2,
        "name": "Motion"
      },
      {
        "id": 3,
        "name": "Contract"
      }
    ]
  }
  ```

### 8. Bulk Upload Documents
- **URL**: `/api/documents/bulk-upload/`
- **Method**: POST
- **Authentication**: Required
- **Description**: Upload multiple documents at once
- **Request Body**: Multipart form data with multiple files
- **Response**:
  ```json
  {
    "success": true,
    "uploaded_count": 3,
    "failed_count": 0,
    "documents": [
      {
        "id": 1,
        "title": "Document 1",
        "status": "success"
      }
    ]
  }
  ```

### 9. Document Statistics
- **URL**: `/api/documents/statistics/`
- **Method**: GET
- **Authentication**: Required
- **Description**: Get document statistics
- **Response**:
  ```json
  {
    "total_documents": 100,
    "total_size_mb": 256.5,
    "by_type": {
      "Evidence": 30,
      "Motion": 45,
      "Contract": 25
    },
    "by_file_type": {
      "pdf": 70,
      "docx": 20,
      "jpg": 10
    }
  }
  ```

## Error Responses

### 400 Bad Request
```json
{
  "status": "error",
  "message": "Invalid data provided",
  "errors": {
    "file": ["File type not supported"],
    "title": ["This field is required"]
  }
}
```

### 401 Unauthorized
```json
{
  "status": "error",
  "message": "Authentication credentials were not provided"
}
```

### 404 Not Found
```json
{
  "status": "error",
  "message": "Document not found"
}
```

### 413 Payload Too Large
```json
{
  "status": "error",
  "message": "File size exceeds maximum limit"
}
```
