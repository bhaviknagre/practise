# Tasks API

API endpoints for managing tasks and related operations.

## Endpoints

### 1. List Tasks
- **URL**: `/api/tasks/`
- **Method**: GET
- **Authentication**: Required
- **Description**: Get a list of all tasks
- **Query Parameters**:
  - `search`: Search by title
  - `status`: Filter by task status
  - `priority`: Filter by priority level
  - `case`: Filter by case ID
  - `assigned_to`: Filter by assigned user ID
  - `is_completed`: Filter completed/incomplete tasks
  - `due_date`: Filter by due date
  - `ordering`: Order by field (e.g., `-due_date`)
- **Response**:
  ```json
  {
    "count": 10,
    "next": "http://api.example.com/api/tasks/?page=2",
    "previous": null,
    "results": [
      {
        "id": 1,
        "title": "File Motion",
        "status": "Pending",
        "priority": "High",
        "case": {
          "id": 1,
          "title": "Smith vs. State"
        },
        "assigned_to": {
          "id": 1,
          "name": "John Doe"
        },
        "due_date": "2025-02-01",
        "is_completed": false
      }
    ]
  }
  ```

### 2. Create Task
- **URL**: `/api/tasks/`
- **Method**: POST
- **Authentication**: Required
- **Description**: Create a new task
- **Request Body**:
  ```json
  {
    "title": "File Motion",
    "description": "Prepare and file motion for dismissal",
    "case": 1,
    "assigned_to": 1,
    "due_date": "2025-02-01",
    "status": 1,
    "priority": 1
  }
  ```
- **Response**: Created task object

### 3. Get Task Details
- **URL**: `/api/tasks/{id}/`
- **Method**: GET
- **Authentication**: Required
- **Description**: Get details of a specific task
- **Response**: Task object with full details

### 4. Update Task
- **URL**: `/api/tasks/{id}/`
- **Method**: PUT/PATCH
- **Authentication**: Required
- **Description**: Update task information
- **Request Body**: Same as Create with optional fields
- **Response**: Updated task object

### 5. Delete Task
- **URL**: `/api/tasks/{id}/`
- **Method**: DELETE
- **Authentication**: Required
- **Description**: Delete a task

### 6. Task Statuses
- **URL**: `/api/tasks/statuses/`
- **Method**: GET
- **Authentication**: Required
- **Description**: Get list of available task statuses
- **Response**:
  ```json
  {
    "statuses": [
      {
        "id": 1,
        "name": "Pending"
      },
      {
        "id": 2,
        "name": "In Progress"
      },
      {
        "id": 3,
        "name": "Completed"
      }
    ]
  }
  ```

### 7. Task Priorities
- **URL**: `/api/tasks/priorities/`
- **Method**: GET
- **Authentication**: Required
- **Description**: Get list of available task priorities
- **Response**:
  ```json
  {
    "priorities": [
      {
        "id": 1,
        "level": "High"
      },
      {
        "id": 2,
        "level": "Medium"
      },
      {
        "id": 3,
        "level": "Low"
      }
    ]
  }
  ```

### 8. Mark Task Complete
- **URL**: `/api/tasks/{id}/complete/`
- **Method**: POST
- **Authentication**: Required
- **Description**: Mark a task as completed
- **Response**:
  ```json
  {
    "id": 1,
    "title": "File Motion",
    "is_completed": true,
    "completed_at": "2025-01-15T10:30:00Z"
  }
  ```

### 9. Task Statistics
- **URL**: `/api/tasks/statistics/`
- **Method**: GET
- **Authentication**: Required
- **Description**: Get task statistics
- **Response**:
  ```json
  {
    "total_tasks": 50,
    "completed_tasks": 30,
    "overdue_tasks": 5,
    "by_priority": {
      "High": 15,
      "Medium": 25,
      "Low": 10
    },
    "by_status": {
      "Pending": 10,
      "In Progress": 10,
      "Completed": 30
    }
  }
  ```

### 10. Bulk Update Tasks
- **URL**: `/api/tasks/bulk-update/`
- **Method**: POST
- **Authentication**: Required
- **Description**: Update multiple tasks at once
- **Request Body**:
  ```json
  {
    "task_ids": [1, 2, 3],
    "updates": {
      "status": 2,
      "priority": 1
    }
  }
  ```
- **Response**:
  ```json
  {
    "updated_count": 3,
    "failed_count": 0
  }
  ```

## Error Responses

### 400 Bad Request
```json
{
  "status": "error",
  "message": "Invalid data provided",
  "errors": {
    "due_date": ["Due date cannot be in the past"],
    "case": ["Case does not exist"]
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
  "message": "Task not found"
}
```

### 403 Forbidden
```json
{
  "status": "error",
  "message": "You do not have permission to modify this task"
}
```
