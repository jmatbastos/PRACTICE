from flask import session
import pymysql.cursors
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



def get_jobs(category_id = None):
    pass

def get_job_categories():
    pass

def get_myapplications():
    pass


def make_application(job_id,motivation,salary, cv):
    pass


   