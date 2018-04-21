from flask import Flask,render_template,request,url_for,redirect
from website_sentiment_db import sentiment
from MySQLdb import escape_string as thwart
from dbconn import connection
from textblob import TextBlob
import gc


app = Flask(__name__)

@app.route('/result',methods=['GET','POST'])
def result():
    return render_template('result.html',webname=request.args.get('webname'),message=request.args.get('message'))


@app.route('/review', methods=['GET','POST'])
def review():
    if request.method == 'POST':
        website = request.form['website']
        user_review = request.form['user_review']
        c, conn = connection()

        c.execute("INSERT INTO review (webname,review) VALUES(%s,%s)", (thwart(website),thwart(user_review)))
        conn.commit()

        c.close()
        conn.close()
        gc.collect()
        
        return render_template('review.html')
        
    return render_template('review.html')

@app.route('/', methods=['GET','POST'])
def homepage():
    if request.method == 'POST':
        search = request.form['search']
        senti = sentiment(search)
        print(senti)
        return redirect(url_for('result',webname=search.title(),message=str(int(senti[2]))))

    return render_template('index.html')
    
# Main Method
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
