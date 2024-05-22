# SocialMedia

SocialMedia is a Django-based web application that allows users to create, join, and participate in groups based on shared interests. Users can post messages, comment on posts, and interact with other group members.

## Features

- User authentication and profile management
- Create and join interest-based groups
- Post messages and comments within groups
- Real-time notifications for group activities
- Responsive design for mobile and desktop

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Marjol-Mata/SocialMedia.git
    cd SocialMedia
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Create a `.env` file for environment variables:
    ```env
    DEBUG=True
    SECRET_KEY=your-secret-key
    DATABASE_URL=sqlite:///db.sqlite3
    ```

4. Apply migrations and start the server:
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

## Usage

1. Open your browser and go to `http://127.0.0.1:8000/` to view the application.
2. Register a new account or log in with an existing account.
3. Create, join, and participate in groups.
