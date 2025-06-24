# Lawyer API

API endpoints for managing lawyer profiles and related operations.

## Endpoints

### 1. List Lawyers
- **URL**: `/api/lawyers/`
- **Method**: GET
- **Authentication**: Required
- **Description**: Get a list of all lawyers
- **Query Parameters**:
  - `search`: Search by name or specialization
  - `specialization`: Filter by specialization
  - `is_verified`: Filter by verification status
  - `ordering`: Order by field (e.g., `-joined_date`)
- **Response**:
  ```json
  {
    "count": 10,
    "next": "http://api.example.com/api/lawyers/?page=2",
    "previous": null,
    "results": [
      {
        "id": 1,
        "user": {
          "username": "lawyer1",
          "email": "lawyer1@example.com",
          "first_name": "John",
          "last_name": "Doe"
        },
        "mobile_number": "+1234567890",
        "specialization": "Criminal Law",
        "years_of_experience": 10,
        "rating": 4.5,
        "is_verified": true
      }
    ]
  }
  ```

### 2. Create Lawyer Profile
- **URL**: `/api/lawyers/`
- **Method**: POST
- **Authentication**: Required
- **Description**: Create a new lawyer profile
- **Request Body**:
  ```json
  {
    "mobile_number": "+1234567890",
    "address": "123 Law Street",
    "bar_association_id": "BAR123",
    "specialization": "Criminal Law",
    "bio": "Experienced criminal lawyer",
    "years_of_experience": 10,
    "languages_spoken": "English, Spanish"
  }
  ```
- **Response**: Created lawyer profile object

### 3. Get Lawyer Profile
- **URL**: `/api/lawyers/{id}/`
- **Method**: GET
- **Authentication**: Required
- **Description**: Get details of a specific lawyer
- **Response**: Lawyer profile object

### 4. Update Lawyer Profile
- **URL**: `/api/lawyers/{id}/`
- **Method**: PUT/PATCH
- **Authentication**: Required
- **Description**: Update lawyer profile details
- **Request Body**: Same as Create with optional fields
- **Response**: Updated lawyer profile object

### 5. Delete Lawyer Profile
- **URL**: `/api/lawyers/{id}/`
- **Method**: DELETE
- **Authentication**: Required
- **Description**: Delete a lawyer profile

### 6. Get Lawyer Cases
- **URL**: `/api/lawyers/{id}/cases/`
- **Method**: GET
- **Authentication**: Required
- **Description**: Get all cases handled by a lawyer
- **Query Parameters**:
  - `status`: Filter by case status
  - `is_active`: Filter active/inactive cases
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
        "title": "Smith vs. State",
        "case_number": "CR2025-001",
        "status": "Active",
        "filing_date": "2025-01-15"
      }
    ]
  }
  ```

### 7. Get Lawyer Statistics
- **URL**: `/api/lawyers/{id}/statistics/`
- **Method**: GET
- **Authentication**: Required
- **Description**: Get lawyer's performance statistics
- **Response**:
  ```json
  {
    "total_cases": 50,
    "active_cases": 10,
    "closed_cases": 40,
    "success_rate": 85,
    "average_rating": 4.5,
    "cases_by_type": {
      "Criminal": 20,
      "Civil": 30
    }
  }
  ```

### 8. Update Profile Picture
- **URL**: `/api/lawyers/{id}/profile-picture/`
- **Method**: POST
- **Authentication**: Required
- **Description**: Upload or update profile picture
- **Request**: Multipart form data with image
- **Response**: Updated lawyer profile with new image URL

## Error Responses

### 400 Bad Request
```json
{
  "status": "error",
  "message": "Invalid data provided",
  "errors": {
    "mobile_number": ["Invalid phone number format"],
    "years_of_experience": ["Must be a positive integer"]
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
  "message": "Lawyer profile not found"
}
```
