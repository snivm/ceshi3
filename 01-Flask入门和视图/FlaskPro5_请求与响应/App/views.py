# 蓝图
# 路径和视图函数
from flask import (
    Blueprint,
    request,
    jsonify,
    render_template,
    make_response,
    redirect,
    url_for,
)

# 创建一个蓝图对象
blue = Blueprint("user", __name__)


# 定义一个路由，当访问根路径时，返回'Hello World!'
@blue.route("/")
def hello_world():  # put application's code here
    return "Hello World!"


# 定义一个路由，当访问'/request/'路径时，返回请求信息
@blue.route(
    "/request/", methods=["GET", "POST"]
)  # <Request 'http://127.0.0.1:5000/request/' [GET]>
def get_request():
    pass
    # 打印请求方法
    print(request.method)
    # 打印请求参数
    print(request.args)  # <QueryArgs {'name': ['lisi'], 'age': ['33']}>
    # 打印表单数据
    print(request.form)
    # 打印表单数据中name字段的值
    print(request.form.getlist("name"))
    # 打印请求路径
    print(request.path)  # /request/ 请求路径
    # 打印请求url
    print(request.url)  # /request/?name=lisi&age=33 请求url
    # 打印请求url
    print(request.base_url)  # /request/ 请求url
    # 打印请求url
    print(request.host_url)  # http://127.0.0.1:5000/request/ 请求url

    # coookie
    # 打印cookie
    print(request.cookies)
    return "request_ok!"


@blue.route("/login_error")
def login_error():
    # 创建响应内容：错误信息 + 3秒自动跳转
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


# 定义一个路由，当访问'/response/'路径时，返回响应信息
@blue.route("/response/")
def get_response():
    pass
    # 响应的几种方式
    # 1.直接返回字符串
    # return 'response Ok!'

    # 2. 模版渲染 (一般用于前后端不分离）
    # return render_template('index.html', name='张三', age=33)

    # 3. 返回json数据（前后端分离）
    # data = {'name':'李四','age':44}
    # # return data
    #
    # #jsonify(): 序列化，字典=>字符串
    # return jsonify(data)

    # 4. 自定义Response对象
    # 渲染模板
    html = render_template("templates/index.html", name="张三", age=33)
    # 打印渲染后的html
    print(html, type(html))

    # 创建一个Response对象
    res = make_response(html, 200)
    return res


@blue.route("/redirect/")
def make_redirect():
    pass
    # 重定向的几种方式
    # return redirect('https://www.qq.com')
    # return redirect('/response/')

    # url_for('蓝图名称.视图函数名')
    # ret = url_for('user.get_response')
    # print('ret',ret)
    # return redirect(ret)
    ret2 = url_for("user.get_request", name="王五", age=66)
    return redirect(ret2)
