from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.dth7vdb.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/profile', methods=["POST"]) #프로필 생성
def profile_create():
    name_receive = request.form["name_give"]
    age_receive = request.form["age_give"]
    hobby_receive = request.form["hobby_give"]
    mbti_receive = request.form["mbti_give"]
    goal_receive = request.form["goal_give"]
    food_receive = request.form["food_give"]

    profile_list = list(db.profile.find({}, {'_id': False}))
    count = len(profile_list) + 1

    doc = {
        'number':count,
        'name':name_receive,
        'age':age_receive,
        'hobby':hobby_receive,
        'mbti':mbti_receive,
        'goal':goal_receive,
        'food':food_receive,
        'like':0
    }

    db.profile.insert_one(doc)
    return jsonify({'msg':'등록 완료!'})

@app.route('/profile', methods=["GET"]) #프로필 조회
def profile_read():
    all_profiles = list(db.profile.find({},{'_id':False}))
    return jsonify({'result':all_profiles})

@app.route('/profile/updatehtml<profile_update>') #프로필 수정화면 이동
def updatehtml(profile_update):
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

    db.profile.update_one({'number':int(number_receive)},
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

@app.route('/profile/<int:number>/likes', methods=['PUT'])  #좋아요 버튼
def profile_like(number):
    profile = db.profile.find_one({'number': number})
    like = profile['like']

    db.profile.update_one(
        {'number': number},
        {'$set': {
            'like':like+1
        }}
    )
    return jsonify({'msg':'좋아요!'})

@app.route('/getbefore', methods=["POST"]) #프로필 수정 초기화면 조회
def profile_before():
    number_receive = request.form["number_give"]
    profile_data = db.profile.find_one({'number':int(number_receive)}, {'_id':False})
    return jsonify({'result': profile_data})
   
@app.route('/profile/delete', methods=["DELETE"]) #프로필 삭제
def profile_delete():
    profile_delete = request.form['profile_delete']
    all_profiles = list(db.profile.find({}))
    for number in all_profiles:
        check = number['number']
        if int(check) == int(profile_delete):
            db.profile.delete_one({'number':int(profile_delete)})
        if int(check) > int(profile_delete):
            db.profile.update_one({'number':check},{'$set':{'number':int(check)-1}})

    return jsonify({'msg': "삭제 완료!"})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)