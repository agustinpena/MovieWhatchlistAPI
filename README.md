# MovieWatchlistAPI 🎬

A secure and RESTful API built with Django REST Framework for managing your personal movie watchlist. Users can create, read, update, and delete movie entries, all securely tied to their personal account.

## ✨ Features

*   **RESTful Design:** Clean JSON API endpoints for full CRUD (Create, Read, Update, Delete) operations.
*   **User Authentication:** Secure user authentication ensuring data privacy and security.
*   **Data Isolation:** Users can only access and manipulate their own movie entries.
*   **Database Modeling:** Robust data structure using Django Models with a relational database.
*   **Browsable API:** Developer-friendly interface for exploring and testing API endpoints.

## 🛠️ Tech Stack

*   **Backend Framework:** Python, Django, Django REST Framework (DRF)
*   **Database:** SQLite (Development), ready for MySQL/PostgreSQL (Production)
*   **Authentication:** Session Authentication & Basic Authentication
*   **API Testing:** Thunder Client / Postman

## 🚀 Installation & Setup

Follow these steps to get the project running on your local machine.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/agustinpena/MovieWatchlistAPI.git
    cd MovieWatchlistAPI
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # On macOS/Linux:
    python -m venv venv
    source venv/bin/activate

    # On Windows:
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser account (to access the admin site and API):**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create a username, email, and password.

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7.  **Access the application:**
    *   **API Root:** Navigate to `http://127.0.0.1:8000/api/` in your browser.
    *   **Admin Interface:** Access `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.

## 📚 API Endpoints

| Method | Endpoint | Description | Authentication |
| :--- | :--- | :--- | :--- |
| GET | `/api/movies/` | Retrieve all movies for the authenticated user. | Required |
| POST | `/api/movies/` | Create a new movie entry. | Required |
| GET | `/api/movies/{id}/` | Retrieve details of a specific movie. | Required |
| PUT | `/api/movies/{id}/` | Update all fields of a specific movie. | Required |
| PATCH | `/api/movies/{id}/` | Partially update a specific movie. | Required |
| DELETE | `/api/movies/{id}/` | Delete a specific movie. | Required |

**Authentication:** All endpoints require the user to be logged in. Use Session Authentication in the browser or Basic Authentication in API clients like Thunder Client or Postman.

### Example Usage with Thunder Client/Postman

1.  Set the request URL to `http://127.0.0.1:8000/api/movies/`.
2.  Set the authentication type to **Basic Auth**.
3.  Enter the username and password of your Django user.
4.  For **POST** requests, set the body type to **JSON** and provide data like:
    ```json
    {
      "title": "Inception",
      "genre": "sci-fi",
      "release_year": 2010,
      "watched": true
    }
    ```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page or open a new one to start a discussion.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
