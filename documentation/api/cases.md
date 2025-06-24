# Cases API

API endpoints for managing legal cases and related operations.

## Endpoints

### 1. List Cases
- **URL**: `/api/cases/`
- **Method**: GET
- **Authentication**: Required
- **Description**: Get a list of all cases
- **Query Parameters**:
  - `search`: Search by title or case number
  - `status`: Filter by case status
  - `case_type`: Filter by case type
  - `lawyer`: Filter by lawyer ID
  - `client`: Filter by client ID
  - `court`: Filter by court
  - `is_active`: Filter active/inactive cases
  - `ordering`: Order by field (e.g., `-created_at`)
- **Response**:
  ```json
  {
    "count": 10,
    "next": "http://api.example.com/api/cases/?page=2",
    "previous": null,
    "results": [
      {
        "id": 1,
        "title": "Smith vs. State",
        "case_number": "CR2025-001",
        "status": "Active",
        "case_type": "Criminal",
        "lawyer": {
          "id": 1,
          "name": "John Doe"
        },
        "client": {
          "id": 1,
          "name": "Jane Smith"
        },
        "filing_date": "2025-01-15"
      }
    ]
  }
  ```

### 2. Create Case
- **URL**: `/api/cases/`
- **Method**: POST
- **Authentication**: Required
- **Description**: Create a new case
- **Request Body**:
  ```json
  {
    "title": "Smith vs. State",
    "description": "Criminal defense case",
    "status": 1,
    "case_type": 1,
    "lawyer": 1,
    "client": 1,
    "opposing_party": 1,
    "court": 1,
    "judge": 1,
    "case_number": "CR2025-001",
    "filing_date": "2025-01-15"
  }
  ```
- **Response**: Created case object

### 3. Get Case Details
- **URL**: `/api/cases/{id}/`
- **Method**: GET
- **Authentication**: Required
- **Description**: Get details of a specific case
- **Response**: Case object with full details

### 4. Update Case
- **URL**: `/api/cases/{id}/`
- **Method**: PUT/PATCH
- **Authentication**: Required
- **Description**: Update case information
- **Request Body**: Same as Create with optional fields
- **Response**: Updated case object

### 5. Delete Case
- **URL**: `/api/cases/{id}/`
- **Method**: DELETE
- **Authentication**: Required
- **Description**: Delete a case

### 6. Get Case Documents
- **URL**: `/api/cases/{id}/documents/`
- **Method**: GET
- **Authentication**: Required
- **Description**: Get all documents related to a case
- **Query Parameters**:
  - `document_type`: Filter by document type
  - `ordering`: Order by upload date
- **Response**:
  ```json
  {
    "count": 5,
    "results": [
      {
        "id": 1,
        "title": "Evidence Document",
        "document_type": "Evidence",
        "uploaded_by": {
          "id": 1,
          "name": "John Doe"
        },
        "uploaded_at": "2025-01-15T10:30:00Z"
      }
    ]
  }
  ```

### 7. Get Case Tasks
- **URL**: `/api/cases/{id}/tasks/`
- **Method**: GET
- **Authentication**: Required
- **Description**: Get all tasks related to a case
- **Query Parameters**:
  - `status`: Filter by task status
  - `priority`: Filter by priority
  - `assigned_to`: Filter by assigned user
- **Response**:
  ```json
  {
    "count": 3,
    "results": [
      {
        "id": 1,
        "title": "File Motion",
        "status": "Pending",
        "priority": "High",
        "assigned_to": {
          "id": 1,
          "name": "John Doe"
        },
        "due_date": "2025-02-01"
      }
    ]
  }
  ```

### 8. Case Timeline
- **URL**: `/api/cases/{id}/timeline/`
- **Method**: GET
- **Authentication**: Required
- **Description**: Get case timeline events
- **Response**:
  ```json
  {
    "events": [
      {
        "date": "2025-01-15",
        "event_type": "Case Filing",
        "description": "Case filed with court"
      },
      {
        "date": "2025-01-20",
        "event_type": "Document Upload",
        "description": "Evidence documents uploaded"
      }
    ]
  }
  ```

### 9. Case Statistics
- **URL**: `/api/cases/{id}/statistics/`
- **Method**: GET
- **Authentication**: Required
- **Description**: Get case statistics
- **Response**:
  ```json
  {
    "days_active": 30,
    "total_documents": 15,
    "total_tasks": 8,
    "completed_tasks": 5,
    "upcoming_deadlines": 3
  }
  ```

## Error Responses

### 400 Bad Request
```json
{
  "status": "error",
  "message": "Invalid data provided",
  "errors": {
    "case_number": ["This case number already exists"],
    "filing_date": ["Filing date cannot be in the future"]
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
  "message": "Case not found"
}
```

### 403 Forbidden
```json
{
  "status": "error",
  "message": "You do not have permission to access this case"
}
```
