# Simple Note-Taking API

# Description
This Django-based API allows users to create, retrieve, update, and query notes by title. The API also includes documentation using Swagger UI and Redoc.


## Setup Instructions

1. Clone the repository:
    ```
    git clone https://github.com/amitkumar0198singh/Note-Application.git
    cd Note-Application
    ```

2. Create a virtual environment and activate it:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Run the server:
    ```
    python manage.py runserver
    ```

6. Access Swagger API documentation at:
    ```
    http://127.0.0.1:8000/swagger/
    ```


# Features

1. Create a new note: 
    ```
    Add new notes to the database.
    ```

2. Retrieve all notes: 
    ```
    Get a list of all notes.
    ```

3. Retrieve a note by ID: 
    ```
    Fetch a specific note by its ID.
    ```

4. Query notes by title: 
    ```
    Search for notes using a title substring.
    ```

5. Swagger and Redoc documentation:
    ```
    Interactive API documentation for ease of use.
    ```

## API Endpoints

- `POST /notes/`: Create a new note.
- `GET /notes/ or /notes/<id>/`: Retrieve all notes or a specific note by its ID.
- `GET /notes?title=<substring>`: Query notes by title.
- `PUT /notes/<id>/`: Update a note by ID.




# API Documentation
```
This project provides interactive API documentation using Swagger and Redoc.
```

- `GET /schema/swagger-ui/`: Swagger UI
- `GET /schema/redoc/`: Redoc UI
- `GET /schema/`: OpenAPI Schema