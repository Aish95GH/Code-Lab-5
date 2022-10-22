from flask import Flask, Request, render_template, request
import os
import json
from urllib.request import urlopen 
import requests


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_recommendation():
    api_host=os.environ.get('API_HOST')
    api_port=os.environ.get('API_PORT')
    url = f'http://{api_host}:{api_port}'
    res=requests.get(url)
    food_item=res.text

    return render_template('index.html', food=food_item)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("CONSUMER_PORT"))

    