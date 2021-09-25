import os
import sys
import cx_Oracle
from flask import Flask ,render_template, request, redirect, url_for,session

import random
import datetime
from datetime import date,timedelta
import re
import string

db_user = os.environ.get('DBAAS_USER_NAME', 'sys as sysdba')
db_password = os.environ.get('DBAAS_USER_PASSWORD', 'ORACLE')
db_connect = os.environ.get('DBAAS_DEFAULT_CONNECT_DESCRIPTOR', "localhost:1521/ORCL")
service_port = port=os.environ.get('PORT', '1521')

cx_Oracle.init_oracle_client(lib_dir="C:\\Users\\tejup\\Downloads\\asg\\instantclient_19_12")

app = Flask("Sreyas")

app.secret_key = 'your secret key'

@app.route('/')
def index():
    return render_template('login.html')




@app.route('/login',methods=['GET','POST'])
def login():
    EMAIL = request.form['EMAIL']
    Password=request.form['Password']
    session['username']=EMAIL
    session['password']=Password
    connection = cx_Oracle.connect('SYSTEM/oracle@localhost')
    cur = connection.cursor()
    cur.execute("""SELECT * FROM CUSTOMER where EMAIL=:EMAIL and c_pass=:Password""",EMAIL=EMAIL,Password=Password)
    connection.commit()
    cur.close()
    connection.close()
    return render_template('home.html',s=session)
    




