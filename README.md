# Fusion Design Ecommerce Server | Django Backend

## Table of Contents

1. [About the Project](#about-the-project)
2. [Technologies](#technologies)
3. [Folder Structure](#folder-structure)
4. [Getting Started](#getting-started)
5. [Future Plans](#future-plans)

## About the Project

This Django backend serves as the server-side component for the Fusion Design Ecommerce platform, a high-end e-commerce solution built with NextJS on the frontend. The backend is designed to provide robust e-commerce functionalities, including user authentication, product management, order processing, and real-time data updates. It supports the frontend by handling dynamic product listings, managing user data, and processing transactions, ensuring a seamless and efficient online shopping experience.

## Technologies

The server is built using several key technologies essential for modern backend development:

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Django REST framework**: A powerful and flexible toolkit for building Web APIs, essential for the backend's RESTful services.
- **SQLite**: The default database used for development, easy to set up, and sufficient for initial stages or small-scale applications.
- **Django CORS Headers**: A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses, crucial for allowing frontend requests.

## Folder Structure

The backend project is organized into key directories and files:

- `ecommerce_server/`: Main application directory containing the Django models, views, and serializers.
- `fusion_design_server/`: Project directory with settings and configurations.
- `media/`: Directory for uploaded media files, organized by type (images, etc.).

## Getting Started

To set up and run the Django server locally:

1. **Clone the repository:**
   `git clone https://github.com/Jaron-S/fusion_design_server`

2. **Set up your environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   `pip install -r requirements.txt`

4. **Initialize the database:**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the server:**
   python manage.py runserver
   Access the server at http://localhost:8000.

## Future Plans

The development roadmap includes expanding the backend functionalities to support scalable e-commerce features like advanced product search, personalized user recommendations, and integration with additional payment gateways. Continuous improvements in security, performance, and user experience are also prioritized to adapt to evolving e-commerce trends and customer expectations.
