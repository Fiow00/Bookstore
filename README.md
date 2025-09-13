# Django Bookstore

A professional Django project for managing books, users, and reviews. Features custom user authentication, book management, reviews, media uploads, and a modern admin interface.

## Features

- Custom user model with email authentication
- Book listing, detail, and search views
- Book reviews with user association
- Media uploads for book covers
- Django admin with customizations
- User authentication via [django-allauth](https://github.com/pennersr/django-allauth)
- Responsive templates with Bootstrap 5 and crispy-forms
- Debug toolbar for development
- Production-ready Docker setup

## Project Structure

```
accounts/       # Custom user app
books/          # Book and review models, views, templates
pages/          # Static pages (home, about)
django_project/ # Project settings and URLs
media/          # Uploaded media files (book covers)
staticfiles/    # Collected static files
templates/      # Shared and app-specific templates
```

## Getting Started

### Prerequisites

- Python 3.10+
- Docker & Docker Compose

### Quick Start

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Fiow00/django-bookstore.git
    ```


2. **Build and run with Docker Compose:**
    ```sh
    docker-compose up --build
    ```

3. **Apply migrations and create a superuser:**
    ```sh
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser
    ```

4. **Access the site:**
    - App: http://localhost:8000/
    - Admin: http://localhost:8000/anything-but-admin/

### Running Tests

```sh
docker-compose exec web python manage.py test
```


---

**Made with Django 4.0+**
