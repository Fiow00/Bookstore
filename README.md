# Django Bookstore

Django Bookstore is a full-featured web application built with Django, designed to manage and review books. It includes user authentication, book listing, detailed book views, user reviews, and a modern responsive UI. The project demonstrates best practices in Django development, including custom user models, third-party authentication, and deployment-ready settings.

## Features

- User registration, login, and logout (with [django-allauth](https://django-allauth.readthedocs.io/))
- Custom user model for flexibility and security
- Book listing and detail pages with cover images
- User reviews for each book
- Search functionality for books
- Permissions for special book access
- Responsive design with Bootstrap 5 and crispy-forms
- Admin interface for managing books and users
- Dockerized for easy development and deployment

## Getting Started

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Fiow00/django_for_professionals.git
   cd django_for_professionals
   ```

2. **Run with Docker:**
   ```sh
   docker-compose up
   ```

3. **Access the app:**
   - Visit [http://localhost:8000](http://localhost:8000) in your browser.

## Folder Structure

- `accounts` – Custom user model and authentication logic
- `books` – Book and review models, views, and templates
- `pages` – Static pages (home, about)
- `templates` – Project-wide and app-specific templates
- `staticfiles` – Static assets (CSS, JS, images)
- `media` – Uploaded media files (book covers)


---

**Made with Django 4.0+**
