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

@app.route("/calltopheadlines")
def calltopheadlines():
    # print("In top headlines\n\n\n\n\n")
    newsapi = NewsApiClient(api_key='846079b7bf6b4c4bab42531fa9969190')
    top_headlines = newsapi.get_top_headlines(country="us", language='en',page_size=100)
    # print(top_headlines)
    articles=top_headlines["articles"]
    top5=[]
    articlecounter=0
    for item1 in articles:
        if item1["source"]  is None or item1["source"]["id"] is None or item1["source"]["name"] is None or item1["author"]  is None or item1["title"]  is None or item1["description"]  is None or item1["url"]  is None or item1["urlToImage"]  is None or item1["publishedAt"]  is None or item1["content"]  is None : 
            continue
        if item1["source"]=='' or item1["author"]=='' or item1["title"]=='' or item1["description"]=='' or item1["url"]=='' or item1["urlToImage"]=='' or item1["publishedAt"]=='' or item1["content"]=='' : 
            continue
        temp={}
        temp["urlToImage"]=item1["urlToImage"]
        temp["url"]=item1["url"]
        temp["title"]=item1["title"]
        # if(len(item1["description"])>150):
        #     temp["description"]=item1["description"][:100]+".."
        # else :
        #     temp["description"]=item1["description"]  

        #temp["content"]=item1["content"].split('.')[0]
        temp["description"]=item1["description"]
        top5.append(temp)
        #top5[articlecounter]=item1
        articlecounter+=1
        if articlecounter==5:
            break;    
    #print("top5\n")
    #print(top5)
    #jsonanswer=json.dumps(top5)
    response = app.response_class(
        response=json.dumps(top5),
        status=200,
        mimetype='application/json'
    )
    #return jsonanswer
    return response  


    
@app.route("/Purav")
def Purav():
    return "Hello, Purav"
    
if __name__ == "__main__":
    app.run(debug=True)