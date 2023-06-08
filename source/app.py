from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv:')
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

@app.route('/profile/updatehtml', methods=["POST"])
def updatehtml():
    profile_update = request.form['profile_update'] 
    return render_template('update.html', number=profile_update)


@app.route('/profile/update', methods=["POST"]) #프로필 수정
def profile_update():
    number_receive = request.form["number_give"]
    name_receive = request.form["name_give"]
    age_receive = request.form["age_give"]
    hobby_receive = request.form["hobby_give"]
    mbti_receive = request.form["mbti_give"]
    goal_receive = request.form["goal_give"]
    food_receive = request.form["food_give"]

    db.web.update_one({'number':number_receive},
    {'$set':
    {
        'name':name_receive,
        'age':age_receive,
        'hobby':hobby_receive,
        'mbti':mbti_receive,
        'goal':goal_receive,
        'food':food_receive
    }
    })
    return jsonify({'msg': "수정 완료!"})

@app.route('/profile/delete', methods=["DELETE"]) #프로필 삭제
def profile_delete():
    profile_delete = request.form['profile_delete']
    all_profiles = list(db.web.find({}))
    for number in all_profiles:
        check = number['number']
        if int(check) == int(profile_delete):
            db.web.delete_one({'number':int(profile_delete)})
        if int(check) > int(profile_delete):
            db.web.update_one({'number':check},{'$set':{'number':int(check)-1}})

    return jsonify({'msg': "삭제 완료!"})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)