from flask import Flask, render_template, request
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'uuu'


def get_random_quote():
    """Получение случайной цитаты с API"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get('https://quoteslate.vercel.app/api/quotes/random', headers=headers, timeout=10)
        response.raise_for_status()

        return response.json()

    except (requests.exceptions.RequestException, ValueError, KeyError) as e:
        print(f"Ошибка при получении цитаты: {e}")
        return None


@app.route('/', methods=['GET', 'POST'])
def index():
    quote = get_random_quote()
    return render_template('index.html', quote=quote)

