# KuraVerse API

**A social media REST API built with FastAPI and PostgreSQL.**

KuraVerse API is a backend project I'm building to learn more about how social platforms work behind the scenes. It handles core features like user accounts, authentication, posts, and voting.

While working on this project, I've been getting hands-on experience with FastAPI, PostgreSQL, database management, and building REST APIs with Python.

## Features

- **User Management** — Create user accounts and manage user information.
- **Authentication** — User login with password hashing and JWT-based authentication.
- **Post Management** — Create, view, update, and delete posts, depending on user permissions.
- **Voting System** — Upvote and downvote posts.
- **Database Integration** — Store and manage data using PostgreSQL and SQLAlchemy.
- **Database Migrations** — Keep track of database schema changes using Alembic.
- **Interactive API Docs** — Explore and test endpoints through FastAPI's Swagger UI.

## Tech Stack

| Technology | What I use it for |
|---|---|
| Python | Backend development |
| FastAPI | Building the REST API |
| PostgreSQL | Storing application data |
| SQLAlchemy | Working with the database |
| Alembic | Managing database migrations |
| Pydantic | Validating data and defining schemas |
| JWT | Handling authentication tokens |
| Argon2 | Password hashing |
| Uvicorn | Running the application |

## Getting Started

Want to run the project locally? Follow these steps.

### Prerequisites

Before getting started, make sure you have Python, PostgreSQL, and Git installed.

### 1. Clone the repository

```bash
git clone https://github.com/aryan103-it/KuraVerse-API.git
cd KuraVerse-API
```

### 2. Create a virtual environment

**Windows (PowerShell)**

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project's root directory and add your database and authentication settings.

Here's an example:

```env
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_NAME=kuraverse
DATABASE_USERNAME=your_username
DATABASE_PASSWORD=your_password

SECRET_KEY=your_generated_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Make sure these variable names match the ones used in the project's configuration. Replace the example values with your own settings, and keep your actual credentials and secret key out of Git.

### 5. Set up the database

Create a PostgreSQL database that matches your configuration, then run the database migrations:

```bash
alembic upgrade head
```

This applies the migrations and brings the database schema up to the expected version.

### 6. Start the API

```bash
uvicorn app.main:app --reload
```

The API should now be running at:

`http://127.0.0.1:8000`

### API Documentation

FastAPI provides interactive documentation that makes it easy to explore and test the available endpoints.

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Open either link after starting the server to see the API documentation.

## Project Structure

```text
KuraVerse-API/
├── alembic/          # Database migration files
├── app/              # Main application code
├── alembic.ini       # Alembic configuration
├── requirements.txt  # Project dependencies
└── README.md
```

## What I'm Learning

Building KuraVerse API has given me a chance to put my Python knowledge into practice and understand how different parts of a backend fit together.

Some of the things I've been working with include:

- Building REST APIs with FastAPI.
- Connecting a Python application to PostgreSQL using SQLAlchemy.
- Implementing JWT authentication and password hashing.
- Validating requests and organizing API schemas.
- Managing database changes with Alembic.
- Testing endpoints and debugging backend issues.

## Future Improvements

There are still plenty of things I'd like to explore as I continue working on this project, including automated testing, Docker, CI/CD, and improving the deployment workflow.

## Author

**Aryan Baral**

- GitHub: [@aryan103-it](https://github.com/aryan103-it)

---

*Built as a hands-on project while learning Python backend development.*
