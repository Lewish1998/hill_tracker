from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so

from app import db, login, app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5
from time import time 
# import jwt

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
 
    hills = so.relationship('Hill', back_populates='user')
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class Hill(db.Model):
    __tablename__ = 'hills'
    
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(255), index=True)
    distance: so.Mapped[str] = so.mapped_column(sa.Float(255), index=True, nullable=True)
    height: so.Mapped[Optional[str]] = so.mapped_column(sa.Float(255), index=True, nullable=True)
    time: so.Mapped[Optional[str]] = so.mapped_column(sa.Time, index=True, nullable=True)
    latitude: so.Mapped[str] = so.mapped_column(sa.Float(255), index=True, nullable=True)
    longitude: so.Mapped[str] = so.mapped_column(sa.Float(255), index=True, nullable=True)
    
    user_id = so.mapped_column(sa.ForeignKey('users.id'))
    user = so.relationship('User', back_populates='hills')
    

class HillInfo(db.Model):
    __tablename__ = 'hill_info'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    distance = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    difficulty = db.Column(db.String(255), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)