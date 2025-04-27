# 蓝图
from flask import Blueprint

blue = Blueprint("user", __name__)


@blue.route("/")
def hello_world():  # put application's code here
    return "Hello World!"


@blue.route("/login_error")
def login_error():
    # 创建响应内容：错误信息 + 3秒自动跳转
    content = """
    <html>
        <head>
            <meta http-equiv="refresh" content="3;url=/"> 
        </head>
        <body>
            用户名或密码错误！三秒后跳转到指定路径
        </body>
    </html>
    """
    # 创建响应对象
    response = make_response(content)
    return response
