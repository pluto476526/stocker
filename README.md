# Inventory Management API

## Project Overview
Stocker API is a backend application designed using Django and Django REST Framework (DRF). It allows users to manage inventory items by performing CRUD operations, viewing inventory levels, and tracking inventory changes. This project simulates real-world inventory management for a store, ensuring robust user authentication and database interactions.

---

## Features

### 1. Inventory Item Management (CRUD)
- Users can create, read, update, and delete inventory items.
- Each inventory item includes the following attributes:
  - **Name** (Required)
  - **Description**
  - **Quantity** (Required)
  - **Price** (Required)
  - **Category**
  - **Supplier**
  - **Warehouse**
  - **Low Stock Threshold**
  - **Date Added** (Auto-generated)
  - **Last Updated** (Auto-updated)
- Input validation ensures required fields are provided.

### 2. User Management (CRUD)
- Users can perform CRUD operations on their accounts.
- User attributes include:
  - **Username** (Unique)
  - **Email** (Unique)
  - **Password** (Hashed)
- Authentication ensures that only logged-in users can manage inventory items.
- Permissions restrict users to managing only their own inventory items.

### 3. View Inventory Levels
- An endpoint to view current inventory levels for all items.
- Supports optional filters such as:
  - **Category**
  - **Warehouse**
  - **Supplier**
  - **Price Range**
  - **Low Stock** (items below a defined quantity threshold)

### 4. Track Inventory Changes
- Logs inventory quantity changes (e.g., restocking, sales).
- An endpoint displays the inventory change history, including timestamps and the user who made the changes.

### 5. Authentication
- User authentication uses Django’s built-in system.
- Supports token-based authentication (JWT) for secure access.
- Users must log in to view, create, update, or delete inventory items.

### 6. Pagination and Sorting
- Implements pagination to handle large datasets efficiently.
- Sorting options available by:
  - **Name**
  - **Quantity**
  - **Price**
  - **Date Added**

### 7. Deployment
- The API is deployed on [PythonAnywhere](https://Trin985.pythonanywhere.com).

---

## Other Features

### 1. Low Stock Alerts
- Alerts users via in-app notifications when inventory levels fall below a threshold.

### 2. Dynamic Inventory Categories
- Users can add, update, and delete inventory categories dynamically.

### 3. Supplier Management
- Tracks relationships between inventory items and their suppliers.
- Users can manage supplier data (e.g., name, contact information).

### 4. Inventory Reports
- Generate detailed reports showing:
  - Total inventory value
  - Stock levels
  - Sales/restocking history

### 5. Multi-Warehouse Support
- Manage inventory across multiple warehouses.
- Separate inventory levels for each warehouse.

### 6. Barcode Scanning Integration (Pending)
- Planned feature to allow users to add or update inventory by scanning barcodes.

---

## API Endpoints

### Authentication
#### Register User
**POST** `/api/accounts/register/`

**Request:**
```json
{
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "password123"
}
```

**Response:**
```json
{
    "id": 1,
    "username": "testuser",
    "email": "testuser@example.com"
}
```

#### Login User
**POST** `/api/accounts/login/`

**Request:**
```json
{
    "username": "testuser",
    "password": "password123"
}
```

**Response:**
```json
{
    "token": "8cf07e97ec866623cb63a0fb7bff1bd97a45d16d",
    "user_id": 1,
    "username": "pluto"
}
```

---

### Inventory Management
#### Create Inventory Item
**POST** `/api/inventory/`

**Request:**
```json
{
    "name": "Laptop",
    "description": "Gaming laptop",
    "quantity": 10,
    "price": 1200.00,
    "category": "1",
    "supplier": "1",
    "warehouse": "1",
    "stock_level": "3320",
    "reorder_threshold": "100"
}
```

**Response:**
```json
{
    "count": 3,
    "next": "https://trin985.pythonanywhere.com/api/products/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Laptop",
            "description": "Gaming Laptop",
            "price": 1200,
            "category": 1,
            "category_details": {
                "id": 1,
                "name": "Electronics",
                "description": "a cool description"
            },
            "supplier": 1,
            "supplier_details": {
                "id": 1,
                "name": "suplier 001",
                "contact_info": "sup1@email.com"
            },
            "warehouse": 1,
            "warehouse_details": {
                "id": 1,
                "name": "warehouse 1",
                "location": "kismayu",
                "manager_details": {
                    "id": 1,
                    "username": "user-001",
                    "email": "user001@email.com"
                }
            },
            "stock_level": 3320,
            "reorder_threshold": 100,
            "timestamp": "2025-01-11T09:24:19.219091Z",
            "updated_at": "2025-01-11T09:24:19.219131Z"
        },
        {
            "id": 2,
            "name": "product 002",
            "description": "small desc",
            "price": 300,
            "category": 1,
            "category_details": {
                "id": 1,
                "name": "category 001",
                "description": "a cool description"
            },
            "supplier": 1,
            "supplier_details": {
                "id": 1,
                "name": "suplier 001",
                "contact_info": "sup1@email.com"
            },
            "warehouse": 1,
            "warehouse_details": {
                "id": 1,
                "name": "warehouse 1",
                "location": "kismayu",
                "manager_details": {
                    "id": 1,
                    "username": "user-001",
                    "email": "user001@email.com"
                }
            },
            "stock_level": 3320,
            "reorder_threshold": 100,
            "timestamp": "2025-01-11T09:24:28.803508Z",
            "updated_at": "2025-01-11T09:24:28.803558Z"
        }
    ]
}
```
---

## All Endpoints
- **"/api/accounts/register/"**
- **"/api/accounts/login/"**
- **"/api/accounts/users/"**
- **"/api/products/"**
- **"/api/products/<pk:id>/"**
- **"/api/suppliers/"**
- **"/api/suppliers/<pk:id>/"**
- **"/api/warehouses/"**
- **"/api/warehouses/<pk:id>/"**
- **"/api/categories/"**
- **"/api/categories/<pk:id>/"**
- **"/api/stock-transactions/"**
- **"/api/stock-transactions/<pk:int>"**
- **"/api/notifications/"**

## Deployment
- The API is deployed and accessible at: https://Trin985.pythonanywhere.com/api/

---

## Future Improvements
- Implement barcode scanning for easier inventory updates.
- Integrate advanced reporting with customizable filters.

---

## Contributors
- Developer: [pluto985]
- Contact: [peterkibuka420@protonmail.com]

