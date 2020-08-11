#Purav Nisar
from flask import Flask, render_template 
from newsapi import NewsApiClient 
import json
import string
import re
from flask import request 
from flask import jsonify   

app = Flask(__name__)

@app.route("/index3")
def index3():
    print("static")
    #return render_template("index2.html")
    return app.send_static_file("index3.html")

@app.route("/callapi")
def callapi():
    # print("In everything cards")
    newsapi = NewsApiClient(api_key='846079b7bf6b4c4bab42531fa9969190')
    #top_headlines = newsapi.get_top_headlines(sources='cnn,fox-news', language='en',page_size=30)
    every_news = newsapi.get_everything(sources='cnn,fox-news', language='en',page_size=100)
    # print("cards \n\n",every_news)
    response = app.response_class(
        response=json.dumps(every_news),
        status=200,
        mimetype='application/json'
    )
    #return top_headlines
    return response


@app.route("/Purav")
def Purav():
    return "Hello, Purav"
    
if __name__ == "__main__":
    app.run(debug=True)