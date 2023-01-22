from flask import Flask, render_template, request
import requests
from senti import generateScore
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form_data = request.form['text']
        response = requests.get(form_data)
        soup = BeautifulSoup(response.text, 'html.parser')

        tweet_text = soup.find
        scores = generateScore(form_data)
        
        return  render_template('main.html', scores=scores)
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)















