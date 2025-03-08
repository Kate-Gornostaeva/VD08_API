from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    news = None
    quote = None

    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            weather = get_weather(city)
        news = get_news()
        quote = get_quote()

    return render_template('index.html', weather=weather, news=news, quote=quote)

def get_weather(city):
    api_key = "794f37297fd3e407a71d6aab12aa1c5d"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def get_news():
    api_key = "cc1162a387ff4e4fb895df4ccd36e91b"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    return response.json().get("articles", [])

def get_quote():
    api_url = 'https://api.api-ninjas.com/v1/quotes'
    headers = {'X-Api-Key': 'YQ40x/HRALRIeqf/PwrZbQ==OM4SRewf4q5DyMK9'}
    response = requests.get(api_url, headers=headers)
    if response.status_code == requests.codes.ok:
        data = response.json()
        if data:
            return data[0]  # Возвращаем первую цитату
    return None

if __name__ == '__main__':
    app.run(debug=True)