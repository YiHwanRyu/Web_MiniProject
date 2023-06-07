# commit과 push하시기 전에 꼭 branch확인 부탁드립니다!
# main에 하시면 안됩니다!

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# DB주소는 일단 각자 DB로 작성하셔서 확인하면서 진행해주시면 됩니다.
# 추후에 DB통합 할게요!
# 아래 빈 공백
from pymongo import MongoClient
client = MongoClient('mongodb+srv://   /?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def index(): 
   return render_template('index.html') 

@app.route('/profile', methods=["POST"])
def profile_create():
    return

@app.route('/profile/list')
def profile_read():
    return

@app.route('/profile/update', method=["POST"])
def profile_update():
    return

@app.route('/profile/delete', method=["POST"])
def profile_delete():
    return

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)