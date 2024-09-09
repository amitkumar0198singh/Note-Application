# Simple Note-Taking API

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

## API Endpoints

- `POST /api/notes/`: Create a new note.
- `GET /api/notes/<id>/`: Fetch a note by ID.
- `GET /api/notes/query/?title=<substring>`: Query notes by title.
- `PUT /api/notes/<id>/update/`: Update a note by ID.
