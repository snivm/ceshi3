from flask import Blueprint, request, render_template
from .models import *
import random

# 蓝图
blue = Blueprint('user', __name__)


@blue.route('/')
def index():
    return 'index'


# 多表操作
# ----------------------- 一对多 ----------------------- #

# 一对多
# 增加数据
@blue.route('/addgrade/')
def add_grade():
    # 添加班级
    grades = []
    for i in range(10):
        grade = Grade()
        grade.name = f'Jay{i}-{str(random.randint(10, 99))}'
        grades.append(grade)
    try:
        db.session.add_all(grades)
        db.session.commit()
    except Exception as e:
        print('e:', e)
        db.session.rollback()
        db.session.flush()

    return 'OK'

@blue.route('/addstu/')
def add_stu():
    # 添加学生
    students = []
    for i in range(10, 20):
        stu = Student()
        stu.name = f'Lucy{i}'
        stu.age = i
        stu.gradeid = random.randint(31, 32)
        students.append(stu)
    try:
        db.session.add_all(students)
        db.session.commit()
    except Exception as e:
        print('e:', e)
        db.session.rollback()
        db.session.flush()

    return 'OK'


# 修改
@blue.route('/updatestu/')
def update_stu():
    stu = Student.query.first()
    stu.age = 100
    db.session.commit()

    return 'OK'

# 删除
@blue.route('/delstu/')
def del_stu():
    # 删除学生
    stu = Student.query.first()
    db.session.delete(stu)
    db.session.commit()

    return 'OK'

@blue.route('/delgrade/')
def del_grade():
    # 删除班级
    grade = Grade.query.first()
    db.session.delete(grade)
    db.session.commit()

    return 'OK'


# 查询
@blue.route('/getstu/')
def get_stu():
    # 查询某学生所在的班级: 反向引用grade
    stu = Student.query.get(2)
    # print(stu.name, stu.age)
    # print(stu.gradeid, stu.grade, stu.grade.name, stu.grade.id)

    # 查找某班级下的所有学生
    grade = Grade.query.get(32)
    print(grade.name)
    print(grade.students)  # 所有学生
    for stu in grade.students:
        print(stu.name, stu.age)

    return 'OK'


# ----------------------- 多对多 ----------------------- #
# 添加数据
@blue.route('/adduser/')
def add_user():
    # 添加用户
    users = []
    for i in range(10, 14):
        user = UserModel()
        user.name = f'Lucy-{i}'
        user.age = i
        users.append(user)
    try:
        db.session.add_all(users)
        db.session.commit()
    except Exception as e:
        print('e:', e)
        db.session.rollback()
        db.session.flush()

    return 'OK'

@blue.route('/addmovie/')
def add_movie():
    # 添加电影
    movies = []
    for i in range(10, 14):
        moive = Movie()
        moive.name = f'阿凡达-{i}'
        movies.append(moive)
    try:
        db.session.add_all(movies)
        db.session.commit()
    except Exception as e:
        print('e:', e)
        db.session.rollback()
        db.session.flush()

    return 'OK'

@blue.route('/addcollect/')
def add_collect():
    # 用户收藏电影
    user = UserModel.query.get(1)
    movie = Movie.query.get(1)

    user.movies.append(movie)
    db.session.commit()

    return 'OK'


# 查询
@blue.route('/getcollect/')
def get_collect():
    # 查找某用户收藏的所有电影
    user = UserModel.query.get(1)
    print(user.movies)

    # 查找收藏了某电影的所有用户
    movie = Movie.query.get(4)
    print(movie.users)
    print(list(movie.users))

    return 'OK'


# 修改：和单表操作
# 删除
@blue.route('/deluser/')
def del_user():
    # 级联删除
    user = UserModel.query.get(1)
    db.session.delete(user)
    db.session.commit()

    return 'OK'

