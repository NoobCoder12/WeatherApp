🌤️ Django Weather & Thoughts App

A simple Django web application that allows users to:

    Search for current weather data by city name

    Add and view personal thoughts in the form of blog-style posts

    Access separate REST API endpoints for thoughts, weather, and user data

Weather data is fetched from an external API (e.g., OpenWeatherMap). Thoughts are stored locally using Django models.
🚀 Features

    🔍 Search weather by city (via web UI and API)

    🧠 Create and read personal thoughts (mini diary/blog)

    📍 Shows temperature, humidity, wind speed, and weather condition

    🔐 API access control:

        api/thoughts/ — read-only for anonymous users

        api/weather/ — GET only, public

        api/users/ — authenticated users only (view own data)

    🧾 Responsive design with clean layout

    📌 Added favicon for better UX

    🔐 Uses .env file for secure API key storage

📦 Tech Stack

    Python 3

    Django

    Django REST Framework

    HTML, CSS

    OpenWeatherMap API (or compatible API)

⚙️ Setup Instructions

    Clone the repository and navigate into it:

git clone https://github.com/NoobCoder12/django-portal
cd django-portal

    Create a virtual environment:

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

    Install dependencies:

pip install -r requirements.txt

    Set up environment variables:

Create a .env file in the root directory with the following content:

WEATHER_API_KEY=your_api_key_here
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

Replace values with your actual keys and settings.

    Apply migrations and run the development server:

python manage.py migrate
python manage.py runserver

    Open the app in your browser:

Go to http://127.0.0.1:8000/
🛠️ API Endpoints

    /api/thoughts/ — Read-only list of thoughts; accessible without authentication (for portfolio/demo purposes)

    /api/weather/ — Get weather data by city (GET only; proxies external API)

    /api/users/ — Authenticated users only; returns logged-in user's info

📁 Notes

    The favicon is added and served from static files for improved UI experience.

    The site is fully responsive across screen sizes.

    Environment variables must be set locally in a .env file — do not commit this file to version control.

    Media uploads (e.g., images for thoughts) require proper MEDIA_URL and MEDIA_ROOT configuration in settings.py, and URL patterns for development serving.

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Created by NoobCoder12
