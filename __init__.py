from flask import Flask,render_template,request,url_for,redirect
#from opinion import opinion
from dbconn import connection

app = Flask(__name__)



@app.route('/')
def homepage():
    return render_template('main.html')

if __name__ == '__main__':
    app.run()