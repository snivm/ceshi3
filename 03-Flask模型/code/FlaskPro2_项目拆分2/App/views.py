from flask import Blueprint
from .models import *

# 蓝图
blue = Blueprint('user', __name__)


@blue.route('/')
def index():
    return 'index'



