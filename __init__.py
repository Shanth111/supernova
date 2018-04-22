# -*- coding: utf-8 -*-

from flask import Flask,render_template,request,url_for,redirect
from MySQLdb import escape_string as thwart
from website_sentiment_db import review_sentiment_update
from website_sentiment_db import sentiment
from table_name import website_list
from table_name import table_name
from formula import popularity_value
from formula import senti_value
from dbconn import connection
from textblob import TextBlob
import gc


app = Flask(__name__)


@app.route('/aboutus',methods=['GET','POST'])
def about():
    if request.method == 'POST':
        search = request.form['search']
        senti = sentiment(search)
        popularity = popularity_value(senti[0])
        opinion = senti_value(senti[1])
        return redirect(url_for('result',webname=search.title(),popularity=int(popularity),opinion=str(int(opinion))))

    return render_template('about.html')

@app.route('/aboutus/more', methods=['GET','POST'])
def more():
    if request.method == 'POST':
        search = request.form['search']
        senti = sentiment(search)
        popularity = popularity_value(senti[0])
        opinion = senti_value(senti[1])
        return redirect(url_for('result',webname=search.title(),popularity=int(popularity),opinion=str(int(opinion))))

    return render_template('more.html')

@app.route('/review', methods=['GET','POST'])
def review():
    if request.method == 'POST':
        website = request.form['website']
        user_review = request.form['user_review']

        if website.lower() in website_list():
            review_sentiment_update([table_name(website),website,'',user_review])
        else:
            print('Not Found')
        
        return render_template('review.html')
        
    return render_template('review.html')
    

@app.route('/result',methods=['GET','POST'])
def result():
    if request.method == 'POST':
        search = request.form['search']
        senti = sentiment(search)
        popularity = popularity_value(senti[0])
        opinion = senti_value(senti[1])
        return redirect(url_for('result',webname=search.title(),popularity=int(popularity),opinion=str(int(opinion))))
        
    return render_template('result.html',webname=request.args.get('webname'),\
            popularity=request.args.get('popularity'),opinion=request.args.get('opinion'))


@app.route('/', methods=['GET','POST'])
def homepage():
    if request.method == 'POST':
        search = request.form['search']
        senti = sentiment(search)
        popularity = popularity_value(senti[0])
        opinion = senti_value(senti[1])
        return redirect(url_for('result',webname=search.title(),popularity=int(popularity),opinion=str(int(opinion))))

    return render_template('index.html')
    
# Main Method
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
