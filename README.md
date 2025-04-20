Luxury Hotel System

Luxury Hotel System is a Django REST API backend built to manage hotel operations, including reservations, room management, user roles, billing, maintenance, and guest feedback.

🔑 Highlights

Role-based access: Clients, Admins, Receptionists, Technicians

Room and reservation management

Maintenance request tracking

Invoicing and payment handling

JWT authentication and API-ready

🚀 Quick Start

# Clone the repo
$ git clone https://github.com/yourusername/luxury-hotel-system.git
$ cd luxury-hotel-system

# Set up environment
$ python -m venv .venv
$ source .venv/bin/activate  # or .venv\Scripts\activate (Windows)
$ pip install -r requirements.txt

# Apply migrations and create admin
$ python manage.py migrate
$ python manage.py createsuperuser

# Run server
$ python manage.py runserver

Visit http://localhost:8000/api/ to use the API.

