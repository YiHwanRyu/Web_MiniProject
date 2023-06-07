# commit과 push하시기 전에 꼭 branch확인 부탁드립니다!
# main에 하시면 안됩니다!
# page이동 기능은 구현하고 말씀드릴게요 먼저 홈에서 기본적으로 동작한다고 생각하시면 됩니다. 이후에 경로만 수정할게요.
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# DB주소는 일단 각자 DB로 작성하셔서 확인하면서 진행해주시면 됩니다.
# 추후에 DB통합 할게요!
# 아래 빈 공백
from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.4np5gdf.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

comment_url = "/commentData"

# 팬명록 작성코드의 일부를 남겨두었습니다.
@app.route('/')
def home():
   return render_template('index.html')

@app.route(comment_url, methods=["POST"])
def guestbook_post():
    name_receive = request.form['name_give']
    password_receive = request.form['password_give']
    comment_receive = request.form['comment_give']
    comment_list = list(db.comments.find({}, {'_id': False}))
    count = len(comment_list) + 1
    doc = {
        'name':name_receive,
        'password':password_receive,
        'comment':comment_receive,
        'number':count,                  #data마다 고유 값 부여
        'goods':0
    }
    db.comments.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})


@app.route(comment_url, methods=["PUT"])
def goods():
    comment_index = request.form['comment_index']
    db.comments.update_one({'num': int(comment_index)},{'$set':{'goods':goods+1}})
    return jsonify({'msg': '좋아요가 반영되었습니다!'})

@app.route(comment_url, methods=["GET"])
def comment_all_get():
    all_comments = list(db.comments.find({},{'_id':False}))
    return jsonify({'result': all_comments})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)

