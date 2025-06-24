# API Documentation

The LawAI backend provides a comprehensive REST API for managing all aspects of a legal practice. This document provides detailed information about all available endpoints, their methods, required parameters, and response formats.

## API Base URL

All API endpoints are prefixed with `/api/`.

## Available Documentation Formats

The API documentation is available in three formats:

1. Swagger UI: `/swagger/`
2. ReDoc: `/redoc/`
3. Raw OpenAPI Schema: `/swagger.json` or `/swagger.yaml`

## Authentication

All API endpoints except authentication endpoints require authentication. See the [Authentication](../authentication.md) documentation for details.

Include your authentication token in the request header:
```
Authorization: Token <your_token>
```
or
```
Authorization: Bearer <your_jwt_token>
```

## API Endpoints Overview

1. [Lawyer API](./lawyer.md)
2. [Client API](./client.md)
3. [Cases API](./cases.md)
4. [Document API](./document.md)
5. [Tasks API](./tasks.md)

## Common Response Formats

### Success Response
```json
{
    "status": "success",
    "data": {
        // Response data
    },
    "message": "Operation successful"
}
```

### Error Response
```json
{
    "status": "error",
    "message": "Error description",
    "errors": {
        // Detailed error information
    }
}
```

## Pagination

List endpoints support pagination with the following query parameters:
- `page`: Page number (default: 1)
- `page_size`: Number of items per page (default: 10)

Example response:
```json
{
    "count": 100,
    "next": "http://api.example.com/api/items/?page=2",
    "previous": null,
    "results": [
        // Items list
    ]
}
```

## Filtering and Searching

Many list endpoints support filtering and searching using query parameters:

- Search: `?search=query`
- Filter: `?field_name=value`
- Ordering: `?ordering=field_name` or `?ordering=-field_name` (descending)

## Rate Limiting

API endpoints are rate-limited to prevent abuse. Current limits:
- Anonymous users: 100 requests per hour
- Authenticated users: 1000 requests per hour

## Error Codes

Common HTTP status codes used by the API:

- 200: Success
- 201: Created
- 204: No Content
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 429: Too Many Requests
- 500: Internal Server Error
