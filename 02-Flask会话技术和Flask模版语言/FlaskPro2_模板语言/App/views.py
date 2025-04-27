# views.py: 路由 + 视图函数

from flask import Blueprint, render_template
from .models import *

# 蓝图
blue = Blueprint("user", __name__)


@blue.route("/")
def home():
    pass

    data = {
        "name": "ikun",
        "age": 26,
        "likes": ["ball", "sing", "dance", "code"],
    }

    return render_template("home.html", **data)
