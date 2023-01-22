from flask import Flask, render_template, request
import requests
from senti import generateScore
import tweepy
from twitauth import api
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form_data = request.form['text']
        response = requests.get(form_data)
        tweet_id = re.search(r'status\/(\d+)', response.text).group(1)

        try:
            tweet = api.get_status(tweet_id)
            scores = generateScore(tweet.text)
        
        except tweepy.errors.TweepyException as e:
            print(f'Error: {e}')

        return render_template('main.html', scores=scores)
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)