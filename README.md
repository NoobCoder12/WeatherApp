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

1. **Clone the repository**

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo

    Create a virtual environment

python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate

    Install dependencies

pip install -r requirements.txt

    Set up environment variables

Create a .env file in the root directory with the following content:

WEATHER_API_KEY=your_api_key_here

    Apply migrations and run the server

python manage.py migrate
python manage.py runserver

    Open the app

Go to http://127.0.0.1:8000/ in your browser.

Notes
You must create an account on OpenWeatherMap to obtain an API key.

Thoughts/posts are handled with Django forms and displayed in the app.

Media file uploads (like banners for posts) require configuration in settings.py.

License
This project is licensed under the MIT License.

Author
Created by NoobCoder12