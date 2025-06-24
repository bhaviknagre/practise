# Getting Started

This guide will help you set up and run the LawAI backend application.

## Prerequisites

1. Python 3.8 or higher
2. Django 5.2.3
3. PostgreSQL (optional, SQLite for development)
4. Virtual environment tool (venv)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd lawai-backend
```

2. Create and activate virtual environment:
```bash
python -m venv myenv
# On Windows:
myenv\Scripts\activate
# On Unix/MacOS:
source myenv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the project root with:
```env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
```

5. Apply database migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

## Running the Application

1. Start the development server:
```bash
python manage.py runserver
```

2. Access the application:
- Admin interface: `http://127.0.0.1:8000/admin/`
- API documentation: `http://127.0.0.1:8000/swagger/`
- ReDoc documentation: `http://127.0.0.1:8000/redoc/`

## Project Structure

The project is organized into several Django apps:

- `lawyer/`: Lawyer profile management
- `client/`: Client management
- `cases/`: Case management
- `document/`: Document management
- `tasks/`: Task management
- `core/`: Project settings and configuration

## API Authentication

The API uses token-based authentication. To get started:

1. Create an account through the registration endpoint
2. Obtain an authentication token
3. Include the token in request headers:
```
Authorization: Token <your-token>
```

## Development Workflow

1. Create feature branch:
```bash
git checkout -b feature/your-feature-name
```

2. Make changes and run tests:
```bash
python manage.py test
```

3. Check code style:
```bash
flake8
```

4. Create migrations if needed:
```bash
python manage.py makemigrations
```

5. Apply migrations:
```bash
python manage.py migrate
```

## Configuration Options

Key settings in `core/settings.py`:

- `DEBUG`: Development mode
- `ALLOWED_HOSTS`: Allowed hostnames
- `DATABASES`: Database configuration
- `REST_FRAMEWORK`: DRF settings
- `CORS_ALLOWED_ORIGINS`: CORS configuration

## File Storage

Documents are stored in:
- Development: Local filesystem
- Production: Configure appropriate storage backend

## Available APIs

1. Authentication:
   - Registration
   - Login
   - Password reset

2. Lawyer Management:
   - Profile CRUD
   - Statistics

3. Client Management:
   - Client CRUD
   - Client cases

4. Case Management:
   - Case CRUD
   - Documents
   - Tasks

5. Document Management:
   - Upload/Download
   - Organization

6. Task Management:
   - Task CRUD
   - Assignments
   - Status tracking

## Testing

Run tests with:
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test lawyer
python manage.py test cases
```

## Common Issues

1. Migration conflicts:
```bash
python manage.py migrate --fake
python manage.py migrate
```

2. Static files not serving:
```bash
python manage.py collectstatic
```

3. Database reset:
```bash
python manage.py flush
```

## Support

For support and bug reports:
1. Check existing issues
2. Create new issue with:
   - Steps to reproduce
   - Expected behavior
   - Actual behavior
   - Error messages
   - Environment details
