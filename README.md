🌤️ Django Weather & Thoughts App

A simple Django web application that allows users to:

    Search for current weather data by city name

    Add and view personal thoughts in the form of blog-style posts

Weather data is fetched from an external API (weatherapi.com). Thoughts are stored locally using Django models.

🚀 Features

    🔍 Search weather by city

    🧠 Create and read personal thoughts (like a mini diary or blog)

    📍 Shows temperature, humidity, wind speed, and weather condition

    🔐 REST API endpoints using Django REST Framework:

        api/thoughts/ — read-only for everyone (portfolio showcase)

        api/weather/ — fetches weather data from external API, GET only

        api/users/ — user data endpoint, accessible only to authenticated users

    🌐 Responsive design with clean layout

    🔖 Favicon added for site branding

    🔑 Uses .env file for secure API key storage

📦 Tech Stack

    Python 3

    Django

    Django REST Framework

    HTML, CSS

    weatherapi.com API

⚙️ Setup Instructions

    Clone the repository and navigate into it

git clone https://github.com/NoobCoder12/django-portal
cd django-portal

    Create a virtual environment

python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate

    Install dependencies

pip install -r requirements.txt

    Set up environment variables

Create a .env file in the root directory with the following content:

WEATHER_API_KEY=your_weatherapi_key_here
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

Replace values accordingly. The API key is from weatherapi.com.

    Apply migrations and run the server

python manage.py migrate
python manage.py runserver

    Open the app

Go to http://127.0.0.1:8000/ in your browser.

🚀 Deployment

The app is deployed on Render and is publicly available at:
https://weatherapp-k1rj.onrender.com/

📋 Notes

    You must create an account on weatherapi.com to obtain an API key.

    Thoughts/posts are handled with Django forms and displayed in the app.

    Media uploads (like banners for posts) are configured in settings.py. The static/media serving in development is automatically handled based on your DEBUG setting in urls.py.
    
    On production, the app uses PostgreSQL as the database backend.

📄 License

This project is licensed under the MIT License.

👤 Author

Created by NoobCoder12
