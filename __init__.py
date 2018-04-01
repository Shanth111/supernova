from flask import Flask,render_template,request,url_for,redirect
from MySQLdb import escape_string as thwart
from dbconn import connection
from textblob import TextBlob
#from opinion import opinion
import gc


app = Flask(__name__)



@app.route('/', methods=['GET','POST'])
def homepage():
    if request.method == 'POST':
        search = request.form['search']

        c, conn = connection()
        c.execute("SELECT review FROM review WHERE webname='"+search+"'")
        data = c.fetchall()
        #conn.commit()

        c.close()
        conn.close()
        gc.collect()
# Other File
        pol = 0
        for rd in data:
            blob = TextBlob(str(rd))
            pol = pol + blob.sentiment.polarity*100
            print(pol)
# Other File 
        return redirect(url_for('result',search=search,pol=pol))
    return render_template('main.html')

@app.route('/result/<search>/<pol>/',methods=['GET','POST'])
def result(search,pol):
    return render_template('result.html',search=search,pol=pol)


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

    
if __name__ == '__main__':
    app.run()