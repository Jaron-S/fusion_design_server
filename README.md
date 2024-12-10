# Fusion Design E-commerce Server | Django Backend

## Table of Contents

1. [About the Project](#about-the-project)
2. [Live Demo](#live-demo)
3. [Technologies](#technologies)
4. [Folder Structure](#folder-structure)
5. [Getting Started](#getting-started)
6. [Future Plans](#future-plans)

## About the Project

This Django backend is the server-side component for the Fusion Design E-commerce platform, a high-end e-commerce solution built with NextJS on the front end. The backend is designed to provide robust e-commerce functionalities, including user authentication, product management, order processing, and real-time data updates. It supports the front end by handling dynamic product listings, managing user data, and processing transactions, ensuring a seamless and efficient online shopping experience.

## Live Demo

Explore the live functionalities of our application through the following links:

### Frontend

The frontend code is available at [Fusion Design Frontend](https://github.com/Jaron-S/fusion-design-frontend).

### Website Hosting

- **Main Website:**
  - Visit [Fusion Design Ecommerce](https://fusion-design.netlify.app/) to experience the high-end e-commerce platform built with Next.js.

- **Backend Server:**
  - The Django backend server is hosted at [https://ionik.pythonanywhere.com](https://ionik.pythonanywhere.com):
    - **Admin Panel:** Access the Django admin dashboard at `/admin` to manage the application's data effectively.
    - **API Endpoints:**
      - `/api/products` - Fetch product data in JSON format.
      - `/api/categories` - Fetch category data in JSON format.
      - `/api/carousel-items` - Fetch carousel items in JSON format.
    - **HTML Views:**
      - `/products` - View formatted product data.
      - `/categories` - View formatted category data.
      - `/carousel` - View formatted carousel data.

## Technologies

The server is built using modern backend technologies to ensure performance, security, and scalability:

- **Django**: A high-level Python web framework that supports rapid development and clean design.
- **Django REST Framework**: A robust toolkit for building Web APIs, enabling seamless communication with the front end.
- **SQLite**: A lightweight database suitable for development and small-scale applications.
- **Django CORS Headers**: A middleware to manage Cross-Origin Resource Sharing (CORS) policies, essential for frontend-backend interaction.

## Folder Structure

The backend project is organized as follows:

- `ecommerce_server/`: Core application directory with models, views, serializers, and URLs.
- `fusion_design_server/`: Project directory containing settings, configurations, and WSGI/ASGI entry points.
- `media/`: Directory for managing uploaded media files.

## Getting Started

To set up and run the Django server locally:

1. **Clone the repository:**
   ```
   git clone https://github.com/Jaron-S/fusion_design_server
   ```

2. **Set up your environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Initialize the database:**
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the server:**
   ```
   python manage.py runserver
   ```

   Access the server at [http://localhost:8000](http://localhost:8000).

## Future Plans

The roadmap for the backend includes:

- Advanced product search functionalities.
- Personalized user recommendations.
- Integration with multiple payment gateways.
- Enhanced performance optimization and security measures.
- Support for scalable deployment in production environments.
