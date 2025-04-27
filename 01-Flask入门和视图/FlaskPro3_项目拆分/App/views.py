#蓝图
from flask import Blueprint

blue = Blueprint('user',__name__)

@blue.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'