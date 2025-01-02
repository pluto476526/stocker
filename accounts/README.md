# Social Media API

A Django-based API for a social media platform. It supports user registration, authentication, and token-based authorization using Django REST Framework (DRF).

## Features
- User Registration
- Token-Based Authentication
- Custom User Model

---

## Setup Process

### Prerequisites
- Python3 (3.10)
- pip3
- djangorestframework
- pillow

### Steps to Set Up

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd social_media_api
   ```

2. **Run Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
   The API will be available at `http://127.0.0.1:8000/`.

---

## API Endpoints

### User Registration
- **Endpoint**: `/api/accounts/register/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "username": "Trin",
      "email": "trin@email.com",
      "password": "password123",
      "bio": "This is my bio",
      "profile_picture": null
  }
  ```
- **Response**:
  ```json
  {
      "message": "New user registered"
  }
  ```

### User Login
- **Endpoint**: `/api/accounts/login/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "username": "Trin",
      "password": "password123"
  }
  ```
- **Response**:
  ```json
  {
      "token": "abcd1234efgh5678ijkl9012mnop3456",
      "user_id": 1,
      "username": "Trin"
  }
  ```

---

## Overview of the User Model
The project uses a custom user model defined in `accounts/models.py` that extends Django's `AbstractUser`. This model includes additional fields:

- **`bio`**: A text field for the user to describe themselves.
- **`profile_picture`**: An image field for the user's profile picture.
- **`followers`**: A `ManyToManyField` referencing itself, allowing users to follow other users. This field is set to `symmetrical=False`.


---

## Authentication Workflow
1. **Register a User**: Use the `/api/accounts/register/` endpoint to create a new account.
2. **Login**: Use the `/api/accounts/login/` endpoint with valid credentials to obtain an authentication token.
3. **Access Protected Endpoints**: Use the token in the `Authorization` header for subsequent API requests:
   ```
   Authorization: Token <your-token>
   ```

