from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.s6qwrpu.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def index(): 
   return render_template('index.html') 

@app.route('/profile', methods=["POST"]) #create 프로필 생성
def profile_create():
    name_receive = request.form["name_give"]
    age_receive = request.form["age_give"]
    hobby_receive = request.form["hobby_give"]
    mbti_receive = request.form["mbti_give"]
    goal_receive = request.form["goal_give"]
    food_receive = request.form["food_give"]

    profile_list = list(db.web.find({}, {'_id': False}))
    count = len(profile_list) + 1

    doc = {
        'number':count,
        'name':name_receive,
        'age':age_receive,
        'hobby':hobby_receive,
        'mbti':mbti_receive,
        'goal':goal_receive,
        'food':food_receive,
        'done':0,
    }

    db.web.insert_one(doc)
    return jsonify({'msg':'등록 완료!'})

@app.route('/profile', methods=["GET"]) #프로필 조회
def profile_read():
    all_profiles = list(db.web.find({},{'_id':False}))
    return jsonify({'result':all_profiles})


@app.route('/profile/update', methods=["POST"]) #프로필 수정
def profile_update():
    return

@app.route('/profile/delete', methods=["POST"]) #프로필 삭제
def profile_delete():
    return

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)