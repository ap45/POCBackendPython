
# POC Backend Python Project

## Project Structure

```
backendpython/
├── manage.py
├── backend/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── student_course/
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
└── venv/
```

## Getting Started

### Prerequisites

- Python 3.x
- Django 5.x

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/ap45/POCBackendPython.git
   cd POCBackendPython
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the migrations (if applicable):
   ```bash
   python manage.py migrate
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

### Git Commands to Push Code

1. Navigate to your project directory:
   ```bash
   cd /path/to/backendpython
   ```

2. Initialize Git (if not done already):
   ```bash
   git init
   ```

3. Create a `.gitignore` file and add:
   ```
   # Python
   __pycache__/
   *.py[cod]
   *.pyo
   *.pyd
   venv/
   .env

   # Django
   *.log
   *.sqlite3
   /media
   ```

4. Add your files to Git:
   ```bash
   git add .
   ```

5. Commit your changes:
   ```bash
   git commit -m "Initial commit of the backend Django project"
   ```

6. Push your changes:
   ```bash
   git push -u origin main
   ```

### License

This project is licensed under the MIT License.
