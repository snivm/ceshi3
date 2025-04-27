from .exts import db

# 类 => 表
# 类属性 => 表字段
# 对象 => 表的一条数据


class User(db.Model):
    __tablename__ = 'user'  # 表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True)
    age = db.Column(db.Integer, default=1)

    def __repr__(self):
        return self.name

