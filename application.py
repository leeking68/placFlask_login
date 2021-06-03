from flask import url_for, session, Flask, render_template, request, redirect

# session 로그인을 구현해주는(딕셔너리쓰면 꼬임 하나에 하나)
# session 은 유저마다 서로다른 딕셔너리를 부여해줘서 , 그것을 통해서 정보를 주고받고.. 

application = Flask(__name__)
application.secret_key = "qwerasdfzxcv"

# temp.. to compare 
ID = "hello"
PW = "world"

@application.route("/")
def home():
    if "userID" in session:
        return render_template("home.html",username=session.get("userID"),login=True)
    else:
        return render_template("home.html",login=False)

@application.route("/login", methods=["get"])
def login():
    global ID,PW
    _id_ = request.args.get("loginId")
    _password_ = request.args.get("loginPw")
    
    if ID == _id_ and PW == _password_:
        session["userID"] = _id_
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))


@application.route("/logout")
def logout():
    session.pop("userID") #끄기
    return redirect(url_for("home"))


application.run(host = "0.0.0.0",port=5000)