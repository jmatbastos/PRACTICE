from flask import session
import pymysql.cursors
import hashlib
from  datetime import datetime


def get_db():
    db = pymysql.connect(
        host='localhost',
        user='a12345',
        password='PASS',
        database='db_a12345',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
    return db


def register_user(username, email, password):    
    pass

def login_user(email,password):
    pass

def activate_user(activation_digest):
    pass


