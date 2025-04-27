# views.py: 路由 + 视图函数
import datetime

from flask import Blueprint, render_template, request, redirect, session, make_response
from .models import *
from time import sleep
import webbrowser

# 蓝图
blue = Blueprint("users", __name__)


# 首页
@blue.route("/")
@blue.route("/home/")
def home():
    # username = request.cookies.get("user")
    username = session.get("user")

    return render_template("templates/home.html", username=username)


@blue.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("templates/login.html")
    elif request.method == "POST":
        pass
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "lisi" and password == "123":
            response = redirect("/home/")

            # response.set_cookie("user", username)
            session["user"] = username
            session.permanent = True
            return response
        else:
            content = """
                <html>
                    <head>
                        <meta http-equiv="refresh" content="3;url=/home"> 
                    </head>
                    <body>
                        用户名或密码错误！三秒后跳转到指定路径
                    </body>
                </html>
                """
            # 创建响应对象
            response = make_response(content)
            return response


@blue.route("/logout/")
def logout():
    response = redirect("/home/")
    # response.delete_cookie("user")
    session.pop("user")
    session.clear()
    return response
