from flask import Blueprint, request, render_template
from sqlalchemy import desc, and_, not_, or_

# import cryptography
from .models import *

# 蓝图
blue = Blueprint("user", __name__)


@blue.route("/")
def index():
    data = [1, 2, 3, 4]
    print(data)
    return data


# 单表操作：
#    增删改查


# 增：添加数据
@blue.route("/useradd/")
def user_add():
    users = []
    for i in (10, 30):
        u = User()
        u.name = "冰冰" + str(i)
        u.age = i
        users.append(u)  # 将用户对象添加到列表中
        print(users)
    try:
        db.session.add_all(users)  # 在循环外部调用add_all，传递整个用户列表
        db.session.commit()
    except Exception as e:
        db.session.rollback()  # 回滚事务
        return "fail: " + str(e)

    return "success!"


# 删：删除数据
#    找到要删除的数据，然后删除
@blue.route("/userdel/")
def user_del():
    u = User.query.first()  # 查询第一条数据
    db.session.delete(u)
    db.session.commit()

    return "success!"


# 改：修改数据
#    找到要修改的数据，然后修改
@blue.route("/userupdate/")
def user_update():
    u = User.query.first()  # 查询第一条数据
    u.age = 1000
    db.session.commit()

    return "success!"


# 查：查询数据
#   条件
@blue.route("/userget/")
def user_get():
    # all(): 返回所有数据，返回列表
    users = User.query.all()
    # print(users, type(users))  # <class 'list'>
    # print(User.query, type(User.query))  # <class 'flask_sqlalchemy.query.Query'>

    # filter() : 过滤,得到查询集，类似SQL中的where
    users = User.query.filter()
    # print(users, type(users))  # 查询集
    # print(list(users))

    # get()：查询到对应主键的数据对象
    user = User.query.get(8)
    # print(user, type(user))  # User对象 <class 'App.models.User'>
    # print(user.name, user.age)  # 获取数据的属性

    # filter() : 类似SQL中的where
    # filter_by() ： 用于等值操作的过滤
    # users = User.query.filter(User.age==20)
    # users = User.query.filter_by(age=20)
    users = User.query.filter(User.age > 20)  # 可以用于非等值操作
    # print(list(users))  # [冰冰20]

    # first() : 第一条数据
    # first_or_404(): 第一条数据,如果不存在则抛出404错误
    user = User.query.first()
    # user = User.query.filter_by(age=100).first_or_404()
    # print(user)

    # count(): 统计查询集中的数据条数
    users = User.query.filter()
    # print(users.count())  # 20

    # limit() : 前几条
    # offset() : 跳过前几条
    users = User.query.offset(3).limit(4)
    # print(list(users))

    # order_by() : 排序
    users = User.query.order_by("age")  # 升序
    users = User.query.order_by(desc("age"))  # 降序
    # print(list(users))

    # 逻辑运算：and_,or_,not_
    users = User.query.filter(User.age > 20, User.age < 25)  # 且，常用
    users = User.query.filter(and_(User.age > 20, User.age < 25))  # 且
    users = User.query.filter(or_(User.age > 25, User.age < 20))  # 或
    users = User.query.filter(not_(or_(User.age > 25, User.age < 20)))  # 非
    # print(list(users))

    # 查询属性
    # contains('3'): 模糊查找，类似SQL中的like
    users = User.query.filter(User.name.contains("3"))
    # in_(): 其中之一
    users = User.query.filter(User.age.in_([10, 20, 30, 40, 50]))
    # startswith() : 以某子串开头
    # endswith() ： 以某子串结尾
    users = User.query.filter(User.name.startswith("冰"))  #
    users = User.query.filter(User.name.endswith("2"))
    # print(list(users))

    # __gt__: 大于
    users = User.query.filter(User.age.__gt__(25))
    print(list(users))

    return "success"


# 分页，翻页
#  1.手动翻页
#     offset().limit()
#  数据： 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
#  页码：page=1
#  每页显示数量：per_page=5
#   page=1 :  1,2,3,4,5       =>  offset(0).limit(5)
#   page=2 :  6,7,8,9,10      =>  offset(5).limit(5)
#   page=3 :  11,12,13,14,15  =>  offset(10).limit(5)
#   page=4 :  16,17,18,19,20  =>  offset(15).limit(5)
#   ...                            ....
#   page=n :          =>  offset((page-1)*per_page).limit(per_page)


# 2.paginate对象
@blue.route("/paginate/")
def get_paginate():
    # 页码：默认显示第一页
    page = int(request.args.get("page", 1))
    # per_page: 每页显示数据量
    per_page = int(request.args.get("per_page", 5))
    # print(page, type(page))
    # print(per_page, type(per_page))

    # paginate()
    p = User.query.paginate(page=page, per_page=per_page, error_out=False)
    # paginate对象的属性：
    # items：返回当前页的内容列表
    print(p.items)
    # has_next：是否还有下一页
    # print(p.has_next)
    # has_prev：是否还有上一页
    # print(p.has_prev)
    # next(error_out=False)：返回下一页的Pagination对象
    # print(p.next(error_out=False).items)
    # prev(error_out=False)：返回上一页的Pagination对象
    # print(p.prev(error_out=False).items)

    # page：当前页的页码（从1开始）
    print(p.page)
    # pages：总页数
    print(p.pages)
    # per_page：每页显示的数量
    # print(p.per_page)
    # prev_num：上一页页码数
    # print(p.prev_num)
    # next_num：下一页页码数
    # print(p.next_num)
    # total：查询返回的记录总数
    print(p.total)

    return render_template("paginate.html", p=p)
