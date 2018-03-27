from flask import Flask,render_template,request,url_for,redirect
#from opinion import opinion
from dbconn import connection
from MySQLdb import escape_string as thwart
import gc


app = Flask(__name__)



@app.route('/')
def homepage():
    return render_template('main.html')

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
        
        return render_template('main.html')
        
    return render_template('review.html')

    
if __name__ == '__main__':
    app.run()