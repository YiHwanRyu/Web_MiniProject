# commit과 push하시기 전에 꼭 branch확인 부탁드립니다!
# main에 하시면 안됩니다!
# page이동 기능은 구현하고 말씀드릴게요 먼저 홈에서 기본적으로 동작한다고 생각하시면 됩니다. 이후에 경로만 수정할게요.
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# DB주소는 일단 각자 DB로 작성하셔서 확인하면서 진행해주시면 됩니다.
# 추후에 DB통합 할게요!
# 아래 빈 공백
from pymongo import MongoClient
client = MongoClient('mongodb+srv://   /?retryWrites=true&w=majority')
db = client.dbsparta


# 팬명록 작성코드의 일부를 남겨두었습니다.
@app.route('/')
def home(): 
   return render_template('index.html') # 시작시 기본 코드

@app.route("/home", methods=["POST"])
def profile_list():
    return jsonify({'msg': '저장 완료!'})

@app.route("/guestbook", methods=["GET"])
def profile_get():
    all_fans = list(db.guestbook.find({},{'_id':False}))
    return jsonify({'result': all_fans})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)