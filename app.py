from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('snspet.html')

@app.route('/sns', methods=['GET'])
def listing():
    snss = list(db.sns.find({},{'_id': False}))
    return jsonify({'all_snss': snss})

## API 역할을 하는 부분
@app.route('/sns', methods=['POST'])
def saving():
    user_receive = request.form['user_give']
    title_receive = request.form['title_give']
    comment_receive = request.form['comment_give']
    file_receive = request.form['file_give']
    
    doc = {
        'user':user_receive,
        'title':title_receive,
        'file':file_receive,
        'comment':comment_receive
    }

    db.sns.insert_one(doc)

    return jsonify({'msg':'작성 완료!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)