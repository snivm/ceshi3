from enum import unique

from .exts import db


class User(db.Model):
    __tablename__ = "tb_user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True, index=True)
    age = db.Column(db.Integer, default=1)
    sex = db.Column(db.Boolean, default=True)
    salary = db.Column(db.Float, default=100000, nullable=False)
