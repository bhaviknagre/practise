# Client API

API endpoints for managing client information and related operations.

## Endpoints

### 1. List Clients
- **URL**: `/api/clients/`
- **Method**: GET
- **Authentication**: Required
- **Description**: Get a list of all clients
- **Query Parameters**:
  - `search`: Search by name or email
  - `created_after`: Filter by creation date
  - `ordering`: Order by field (e.g., `-created_at`)
- **Response**:
  ```json
  {
    "count": 10,
    "next": "http://api.example.com/api/clients/?page=2",
    "previous": null,
    "results": [
      {
        "id": 1,
        "first_name": "Jane",
        "last_name": "Smith",
        "email": "jane.smith@example.com",
        "phone_number": "+1234567890",
        "created_at": "2025-01-15T10:30:00Z"
      }
    ]
  }
  ```

### 2. Create Client
- **URL**: `/api/clients/`
- **Method**: POST
- **Authentication**: Required
- **Description**: Create a new client record
- **Request Body**:
  ```json
  {
    "first_name": "Jane",
    "last_name": "Smith",
    "email": "jane.smith@example.com",
    "phone_number": "+1234567890",
    "alternate_phone_number": "+0987654321",
    "address": "456 Client Street",
    "date_of_birth": "1990-05-15",
    "gender": "female",
    "occupation": "Teacher",
    "company_name": "City School",
    "referred_by": "John Doe",
    "notes": "Initial consultation scheduled"
  }
  ```
- **Response**: Created client object

### 3. Get Client Details
- **URL**: `/api/clients/{id}/`
- **Method**: GET
- **Authentication**: Required
- **Description**: Get details of a specific client
- **Response**: Client object with full details

### 4. Update Client
- **URL**: `/api/clients/{id}/`
- **Method**: PUT/PATCH
- **Authentication**: Required
- **Description**: Update client information
- **Request Body**: Same as Create with optional fields
- **Response**: Updated client object

### 5. Delete Client
- **URL**: `/api/clients/{id}/`
- **Method**: DELETE
- **Authentication**: Required
- **Description**: Delete a client record

### 6. Get Client Cases
- **URL**: `/api/clients/{id}/cases/`
- **Method**: GET
- **Authentication**: Required
- **Description**: Get all cases associated with a client
- **Query Parameters**:
  - `status`: Filter by case status
  - `is_active`: Filter active/inactive cases
  - `ordering`: Order by field
- **Response**:
  ```json
  {
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
      {
        "id": 1,
        "title": "Smith vs. State",
        "case_number": "CR2025-001",
        "status": "Active",
        "filing_date": "2025-01-15"
      }
    ]
  }
  ```

### 7. Get Client Documents
- **URL**: `/api/clients/{id}/documents/`
- **Method**: GET
- **Authentication**: Required
- **Description**: Get all documents related to a client
- **Query Parameters**:
  - `document_type`: Filter by document type
  - `ordering`: Order by field
- **Response**:
  ```json
  {
    "count": 5,
    "next": null,
    "previous": null,
    "results": [
      {
        "id": 1,
        "title": "Contract Agreement",
        "document_type": "Legal Agreement",
        "uploaded_at": "2025-01-15T10:30:00Z",
        "file_type": "pdf",
        "file_size_kb": 1024
      }
    ]
  }
  ```

### 8. Client Statistics
- **URL**: `/api/clients/{id}/statistics/`
- **Method**: GET
- **Authentication**: Required
- **Description**: Get client's case statistics
- **Response**:
  ```json
  {
    "total_cases": 3,
    "active_cases": 1,
    "closed_cases": 2,
    "total_documents": 15,
    "case_types": {
      "Civil": 2,
      "Criminal": 1
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
    "email": ["Invalid email format"],
    "phone_number": ["Invalid phone number format"]
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
  "message": "Client not found"
}
```
