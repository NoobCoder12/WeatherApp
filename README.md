# 🌤️ Django Weather & Thoughts App

A simple Django web application that allows users to:

- Search for current weather data by city name  
- Add and view personal **thoughts** in the form of blog-style posts  

Weather data is fetched from an external API (e.g., OpenWeatherMap). Thoughts are stored locally using Django models.

---

## 🚀 Features

- 🔍 Search weather by city
- 🧠 Create and read personal thoughts (like a mini diary or blog)
- 📍 Shows temperature, humidity, wind speed, and weather condition
- 🧾 Responsive design with clean layout
- 🔐 Uses `.env` file for secure API key storage

---

## 📦 Tech Stack

- Python 3
- Django
- HTML, CSS
- OpenWeatherMap API (or compatible API)

---

## ⚙️ Setup Instructions

1. Clone the repository and navigate into it

```bash
git clone https://github.com/NoobCoder12/django-portal
cd django-portal

2. Create a virtual environment

python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Set up environment variables

Create a .env file in the root directory with the following content:

WEATHER_API_KEY=your_api_key_here

Replace your_api_key_here with your actual API key from OpenWeatherMap.

5. Apply migrations and run the server

python manage.py migrate
python manage.py runserver

6. Open the app

Go to http://127.0.0.1:8000/ in your browser.



Notes

You must create an account on OpenWeatherMap to obtain an API key.

Thoughts/posts are handled with Django forms and displayed in the app.

Media file uploads (like banners for posts) require configuration in settings.py.

To enable media uploads (e.g. banners for posts), ensure you have MEDIA_URL and MEDIA_ROOT configured in settings.py, and add urlpatterns in urls.py during development:

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



License
This project is licensed under the MIT License.

Author
Created by NoobCoder12