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

@app.route("/wordcloud")
def wordcloud():
    # print("In wordcloud\n\n\n\n\n")
    newsapi = NewsApiClient(api_key='846079b7bf6b4c4bab42531fa9969190')
    top_headlines = newsapi.get_top_headlines(country="us", language='en',page_size=100)
    # print("Word cloud top headlines")
    # print(top_headlines)
    articles=top_headlines["articles"]
    #pattern=re.compile("[~`!@#$%^&*()_-+=\';:\"<>,.?\/]")
    wordcount={}
    for item1 in articles:
        titlepunc=item1["title"].translate(item1["title"].maketrans('', '', string.punctuation))
        #titlepunc= re.sub('[\d\W_\n]+', '',item1["title"])
        #titlepunc=item1["title"].string(string.punctuation)
        #titlepunc=item1["title"].replace(pattern,"")
        titlepunc=titlepunc.lower() 
        titlewords=titlepunc.split(' ')
        for w in titlewords:
            if w in wordcount.keys():
                wordcount[w]=wordcount[w]+1
            else:
                wordcount[w]=1
    file1 = open('stopwords_en.txt', 'r') 
    Lines = file1.readlines()
    #stopwords={'was', "t's", 'again', 'wonder', 'two', 'becoming', 'q', 'tries', 'eg', 'needs', 'theirs', 'itself', 'like', 'whereafter', 'is', 'h', 'myself', "it'd", 'went', 'lately', 'while', 'causes', 'using', 'throughout', 'say', 'greetings', 'their', 'mainly', 'whither', 'need', "they'd", 'y', 'anything', 'ask', 'no', 'sensible', 'yet', "who's", 'namely', 'because', 'normally', 'indicated', 'provides', 'of', 'beside', 'c', 'should', 'nd', "i'd", 'welcome', 'hi', 't', 'b', 'thanx', 'sub', "haven't", 'use', 'despite', 'nor', 'exactly', 'them', 'whatever', 'above', 'us', 'o', 'regardless', 'sometime', 'various', 'perhaps', 'indeed', "let's", 'whereby', 'thru', 'well', 'she', "isn't", 'wants', 'ones', "there's", 'want', "i'll", 'even', 'my', 'how', 'currently', 'used', 'next', 'took', "couldn't", 'right', 'everywhere', 'each', 'help', 'inc', 'hereby', 'hello', 'ours', 'once', 'both', 'clearly', 'following', 'meanwhile', 'whom', 'soon', 'unless', 'third', 'aside', 'best', 'however', 'whereupon', 'looks', 'gotten', 'come', 'looking', 'entirely', 'rd', 'certainly', 'try', 'look', 'yourselves', 'across', 'from', 'hither', 'themselves', 'according', 'far', 'second', 'regards', 'g', 'under', 'ok', 'may', 'without', 'less', 'nearly', 'he', 'or', 'when', 'whenever', 'rather', 'whereas', 'little', 'getting', 'thanks', 'thorough', 'seen', 'some', 'the', 'et', 'six', 'doing', 'l', 'changes', 'who', 'for', 'example', 'that', 'none', 'contain', 'we', 'later', 'viz', 'f', 'still', 'thats', 'likely', 'now', 'nine', 'truly', "weren't", 'which', 'latterly', 'though', 'taken', 'beforehand', 'seemed', 'unfortunately', 'mostly', 'herein', "we're", 'do', 'her', 'seeming', 'never', 'sure', 'him', 'former', 'very', 'indicate', 'ought', 'least', 'kept', 'anyways', 'thereby', 'what', 'besides', 'nevertheless', 'himself', 'after', "i'm", 'cannot', 'else', 'had', 'etc', 'down', 'me', 'non', 'behind', 'does', 'downwards', 'self', 'in', 'seven', 'were', 'someone', "they're", 'available', 'nowhere', 'plus', 'respectively', 'around', 're', 'together', "doesn't", "ain't", 'd', 'ex', 'per', 'somewhat', 'below', 'tends', 'tried', 'inner', 'such', 'can', "you'd", 'another', 'take', "that's", 'instead', "won't", 'they', 'insofar', 'usually', 'consider', 'yes', 'different', 'whether', 'r', 'appear', 'regarding', 'particular', 'please', 'concerning', 'a', 'it', "a's", 'cant', 'to', 'course', 'z', 'last', 'probably', 'many', "wasn't", 'an', 'almost', 'anyone', 'up', 'knows', 'lest', "hadn't", 'although', 'qv', 'whence', 'com', 'become', 'brief', 'unto', 'but', 'only', 'zero', 'shall', 'becomes', 'before', 'afterwards', 'particularly', 'presumably', 'out', 'twice', 'via', 'will', 'during', 'thus', 'any', 'off', 'one', 'few', 'associated', 'tell', 'better', 'moreover', 'where', "we'll", 'those', 'edu', 'overall', 'u', 'hardly', 'his', 'then', 'hers', 'our', 'unlikely', 'comes', 'says', "here's", 'sup', "aren't", 'accordingly', 'p', 'described', 'uucp', 'gets', 'ltd', 'wish', 'others', "he's", "they've", "c's", 'along', 'containing', 'e', 'among', 'th', 'think', 'done', 'i', 'necessary', 'get', 'k', 'something', 'alone', 'fifth', 'therefore', 'and', "shouldn't", 'definitely', 'whoever', 'always', 'know', 'am', 'onto', "you'll", 'every', 'already', 'specify', 'happens', 'maybe', 'otherwise', 'relatively', "you're", 'said', 'inward', 'since', 'why', 'quite', 'you', 'came', 'm', 'howbeit', 'whole', 'mean', 'liked', 'whose', 'this', 'at', 'actually', 'five', 's', 'be', 'must', 'been', 'first', 'yours', 'elsewhere', 'formerly', 'hence', 'goes', 'being', 'appreciate', 'are', 'these', 'anyhow', 'novel', 'appropriate', "hasn't", 'nothing', 'other', 'awfully', 'just', 'indicates', 'neither', 'seeing', 'obviously', 'especially', 'therein', 'thank', 'three', 'allow', 'inasmuch', 'sent', 'upon', 'v', 'somewhere', 'furthermore', 'selves', 'trying', 'into', 'having', 'much', 'keep', 'possible', 'until', 'amongst', 'ie', 'same', 'uses', 'saying', 'could', 'became', 'contains', 'have', 'noone', "we've", 'everyone', 'towards', 'against', 'theres', 'by', 'corresponding', 'really', 'ignored', 'several', 'n', 'wherever', 'except', 'specified', "it's", 'apart', 'anywhere', 'cause', 'wherein', 'enough', 'hereafter', 'co', 'placed', 'with', 'thence', 'un', 'if', 'outside', 'willing', 'seem', 'seriously', 'follows', "where's", 'would', 'somehow', 'sorry', 'old', 'away', 'got', 'able', "didn't", 'either', 'has', 'thoroughly', 'beyond', 'latter', 'saw', 'seems', 'there', 'as', 'near', "c'mon", 'somebody', 'asking', 'here', 'oh', 'than', "you've", 'its', 'consequently', 'within', 'all', 'ourselves', 'nobody', 'over', 'followed', 'name', 'through', 'serious', 'x', 'hopefully', 'useful', "what's", 'thereupon', 'see', 'given', 'known', 'going', 'considering', 'most', 'thereafter', "they'll", 'allows', 'about', 'anyway', 'keeps', 'more', 'eight', 'let', 'immediate', 'specifying', "it'll", 'too', 'believe', 'sometimes', "we'd", 'value', 'gives', 'hereupon', "wouldn't", 'not', 'certain', 'w', 'did', 'merely', 'okay', "don't", 'further', 'toward', 'go', 'between', 'everything', 'four', 'often', 'secondly', 'everybody', 'also', "i've", 'way', 'your', 'own', 'new', 'reasonably', 'vs', 'on', 'ever', 'might', 'herself', 'so', 'j', 'forth', 'anybody', 'que', 'gone', 'yourself', "can't"}
    stopwords=set() 
    for line in Lines: 
        stopwords.add(line.strip())
    #print("stopwords",stopwords)    
    wordcountlist=[[k,v] for k,v in wordcount.items()]
    wordcountlist.sort(key = lambda x: x[1],reverse=True)     
    #wordcountsorted =sorted(wordcount.items(), key=operator.itemgetter(1),reverse=True))
    # print(wordcountlist)
    finalwords=[]
    finalwordscounter=0
    for words in wordcountlist:
        if words[0] in stopwords:
            continue
        else:
            finalwords.append(words[0])
            finalwordscounter+=1
        if finalwordscounter==30:
            break
    #print("TOP 30\n\n")
    #print(finalwords)
    wordsdict={}
    wordsdict["finalw"]=finalwords
    finalwordsjson=json.dumps(wordsdict)
    # print("finalwordsjson")
    # print(finalwordsjson)      
    return finalwordsjson

@app.route("/getsources")
def getsources():
    #print("getsources")
   #print(request.url)
    category=request.args.get('value')
    #print("category=",category)
    newsapi = NewsApiClient(api_key='846079b7bf6b4c4bab42531fa9969190')
    if(category=="all"):
        sources = newsapi.get_sources(language="en", country="us")
    else: 
        sources = newsapi.get_sources(category=category, language="en", country="us")
    #print(sources)
    namesources=sources['sources']
    getnames=[]
    if(category=="all"):
        tempcounter=0;
        for item in namesources:
            getnames.append({item['id']:item['name']})
            tempcounter+=1
            if tempcounter>=10:
                break
    else:
        for item in namesources:
            getnames.append({item['id']:item['name']})
    #print("names=",getnames)
    finalnames={}
    finalnames['names']=getnames
    response = app.response_class(
        response=json.dumps(finalnames),
        status=200,
        mimetype='application/json'
    )
    #return render_template("index2.html")
    return response


@app.route("/Purav")
def Purav():
    return "Hello, Purav"
    
if __name__ == "__main__":
    app.run(debug=True)