# Database Models

This document describes the database schema and relationships between different models in the LawAI application.

## Core Models

### LawyerProfile
Represents a lawyer's profile in the system.

```python
class LawyerProfile:
    user: OneToOneField  # Link to Django User model
    mobile_number: CharField
    address: TextField
    bar_association_id: CharField
    specialization: CharField
    bio: TextField
    profile_picture: ImageField
    website: URLField
    joined_date: DateField
    years_of_experience: IntegerField
    total_cases_handled: IntegerField
    languages_spoken: CharField
    rating: FloatField
    is_verified: BooleanField
    last_active: DateTimeField
```

### Client
Represents a client in the system.

```python
class Client:
    first_name: CharField
    last_name: CharField
    email: EmailField
    phone_number: CharField
    alternate_phone_number: CharField
    address: TextField
    date_of_birth: DateField
    gender: CharField  # Choices: male, female, other
    occupation: CharField
    company_name: CharField
    referred_by: CharField
    notes: TextField
    created_at: DateTimeField
    updated_at: DateTimeField
```

### Case
Represents a legal case in the system.

```python
class Case:
    title: CharField
    description: TextField
    status: ForeignKey[CaseStatus]
    case_type: ForeignKey[CaseType]
    lawyer: ForeignKey[LawyerProfile]
    client: ForeignKey[Client]
    opposing_party: ForeignKey[OpposingParty]
    court: ForeignKey[Court]
    judge: ForeignKey[Judge]
    case_number: CharField
    filing_date: DateField
    closing_date: DateField
    payment_status: ForeignKey[PaymentStatus]
    is_active: BooleanField
    created_at: DateTimeField
    updated_at: DateTimeField
```

### Document
Represents legal documents in the system.

```python
class Document:
    title: CharField
    file: FileField
    document_type: ForeignKey[DocumentType]
    case: ForeignKey[Case]
    uploaded_by: ForeignKey[LawyerProfile]
    description: TextField
    uploaded_at: DateTimeField
    updated_at: DateTimeField
    file_type: CharField
    file_size_kb: PositiveIntegerField
```

### Task
Represents tasks associated with cases.

```python
class Task:
    title: CharField
    description: TextField
    case: ForeignKey[Case]
    assigned_to: ForeignKey[User]
    due_date: DateField
    status: ForeignKey[TaskStatus]
    priority: ForeignKey[TaskPriority]
    is_completed: BooleanField
    created_at: DateTimeField
    updated_at: DateTimeField
```

## Supporting Models

### CaseStatus
```python
class CaseStatus:
    name: CharField  # Unique
```

### CaseType
```python
class CaseType:
    name: CharField  # Unique
```

### PaymentStatus
```python
class PaymentStatus:
    status: CharField  # Unique
```

### OpposingParty
```python
class OpposingParty:
    name: CharField
```

### Court
```python
class Court:
    name: CharField  # Unique
```

### Judge
```python
class Judge:
    name: CharField  # Unique
```

### DocumentType
```python
class DocumentType:
    name: CharField  # Unique
```

### TaskStatus
```python
class TaskStatus:
    name: CharField  # Unique
```

### TaskPriority
```python
class TaskPriority:
    level: CharField  # Unique
```

## Relationships

1. LawyerProfile
   - One-to-One with User
   - One-to-Many with Case
   - One-to-Many with Document (uploaded_by)

2. Client
   - One-to-Many with Case

3. Case
   - Many-to-One with LawyerProfile
   - Many-to-One with Client
   - Many-to-One with CaseStatus
   - Many-to-One with CaseType
   - Many-to-One with OpposingParty
   - Many-to-One with Court
   - Many-to-One with Judge
   - Many-to-One with PaymentStatus
   - One-to-Many with Document
   - One-to-Many with Task

4. Document
   - Many-to-One with Case
   - Many-to-One with DocumentType
   - Many-to-One with LawyerProfile (uploaded_by)

5. Task
   - Many-to-One with Case
   - Many-to-One with User (assigned_to)
   - Many-to-One with TaskStatus
   - Many-to-One with TaskPriority
