# Employee Management System

This project implements an Employee Management System with APIs for user authentication, dynamic form creation, and employee management.

---

## Features
1. **User Authentication**
   - Register a user
   - Login with JWT-based authentication
2. **Dynamic Form Creation**
   - Create custom fields for employee details
   - Update employee forms dynamically
3. **Employee CRUD Operations**
   - Add, view, edit, delete employee records

---

## Technology Stack
- Python
- Django
- Django REST Framework
- SQLite (default database)
- Postman for API testing

---

## Installation and Usage

### 1. Prerequisites
Ensure the following are installed on your system:
- Python 3.8+
- Git

---

### 2. Clone the Repository
```bash
git clone https://github.com/JaiseJanet22/EmployeeManagement_jaisejanet22.git
cd EmployeeManagementSystem/backend
```

---

### 3. Set Up a Virtual Environment
1. Create a virtual environment:
   ```bash
   python -m venv env
   ```
2. Activate the virtual environment:
   - On **Windows**:
     ```bash
     .\env\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source env/bin/activate
     ```

---

### 4. Install Dependencies
Install all required Python packages using:
```bash
pip install -r requirements.txt
```

---

### 5. Apply Migrations
Set up the database by running:
```bash
python manage.py migrate
```

---

### 6. Run the Development Server
Start the Django server:
```bash
python manage.py runserver
```
The server will start at `http://127.0.0.1:8000`.

---

## API Endpoints

### **Authentication APIs**
1. **Register**
   - **Endpoint**: `POST /api/auth/register/`
   - **Body (JSON)**:
     ```json
     {
         "username": "testuser",
         "password": "testpass",
         "email": "test@example.com"
     }
     ```

2. **Login**
   - **Endpoint**: `POST /api/auth/login/`
   - **Body (JSON)**:
     ```json
     {
         "username": "testuser",
         "password": "testpass"
     }
     ```

### **Employee Management APIs**
1. **List Employees**
   - **Endpoint**: `GET /api/employees/`

2. **Create Employee**
   - **Endpoint**: `POST /api/employees/`
   - **Body (JSON)**:
     ```json
     {
         "name": "John Doe",
         "email": "john@example.com",
         "phone": "1234567890",
         "address": "123 Main St"
     }
     ```

3. **Update Employee**
   - **Endpoint**: `PUT /api/employees/<id>/`
   - **Body (JSON)**:
     ```json
     {
         "name": "Jane Doe",
         "email": "jane@example.com",
         "phone": "9876543210",
         "address": "456 Elm St"
     }
     ```

4. **Delete Employee**
   - **Endpoint**: `DELETE /api/employees/<id>/`

---

### **Testing APIs with Postman**

#### Import Postman Collection
1. Open Postman.
2. Click **Import** > **Upload Files**.
3. Select the `postman_collection.json` file included in the repository.
4. Test the APIs using the imported requests.

---

### **Common Commands**
- **Run Tests**:
  ```bash
  python manage.py test
  ```
- **Deactivate Virtual Environment**:
  ```bash
  deactivate
  ```
- **Generate New Migrations**:
  ```bash
  python manage.py makemigrations
  ```

---

## Notes
- This project uses SQLite as the default database for simplicity.
- All sensitive information is excluded using `.gitignore`.

---

## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.

---

## License
This project is licensed under the MIT License.




