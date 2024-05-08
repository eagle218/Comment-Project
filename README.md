# Comment Project

A single-page application (SPA) that allows users to leave comments and replies. Each comment is stored in a relational database with identifying user information.

## Features

- Users can leave comments and replies.
- Top-level comments are displayed in a sortable table.
- Replies are displayed nested under their parent comments.
- CAPTCHA protection ensures only genuine users can leave comments.

## Project Structure

```plaintext
comment_project/
│
├── comment_project/  # Django project settings
│   └── __init__.py
│   └── asgi.py
│   └── settings.py
│   └── urls.py
│   └── wsgi.py
│
├── comments/  # Django application
│   └── __init__.py
│   └── models.py
│   └── forms.py
│   └── views.py
│   └── urls.py
│   └── admin.py
│   └── templates/
│       └── comments/
│           └── comment_list.html
│           └── add_comment.html
│           └── reply_list.html
│   └── static/
│       └── comments/
│           └── styles.css
│           └── avatar.png
│
├── manage.py
├── requirements.txt
└── README.md

````

Features
Comments and Replies
    1. Top-level comments are displayed in a sortable table.
    2. Replies are displayed in a nested manner under their parent comments.

CAPTCHA Protection
     CAPTCHA ensures that only genuine users can leave comments.

Getting Started
Prerequisites
Make sure you have the following software installed:

Python 3.8+
    pip package manager
    Git

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/eagle218/dzen-code.git

2. **Change to the project directory:**
     ```bash
   cd comment_project

3. **Install dependencies:**
     ```bash
   pip install -r requirements.txt

4. **Set up the database:**
     ```bash
    python manage.py makemigrations
    python manage.py migrate

5. **Run the development server:**
   ```bash
    python manage.py runserver

