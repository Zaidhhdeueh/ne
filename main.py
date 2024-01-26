from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests
from user_agent import generate_user_agent
useragnet=str(generate_user_agent())
import random
from user_agent import generate_user_agent
app = Flask('app')

@app.route("/login", methods= ["post" , "get"])
def login():
  nme=request.form["input"]
  gg=generate_user_agent()
  email='fhdhasd39123@gmail.com'
  url = "https://www.instagram.com/api/v1/web/accounts/check_email/"
  headers = {
     'accept': '*/*',
     'accept-encoding': 'gzip, deflate, br',
     'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
     'content-length': '30',
     'content-type': 'application/x-www-form-urlencoded',
     'cookie': 'csrftoken=OuvUFtGYLThj0EEZJg62u6bYHxbcXd4b; mid=ZTt78QABAAEbwUSWuNXI7n-622E_; ig_did=3ED5E3B2-A5DF-4087-BFD4-C6C6843F8E5E; ig_nrcb=1; dpr=2.768749952316284; datr=53s7Ze2JEvyfBQKo_WxnTLki',
     'dpr': '2.76875',
     'origin': 'https://www.instagram.com',
     'referer': 'https://www.instagram.com/accounts/signup/email/',
     'sec-ch-prefers-color-scheme': 'dark',
     'sec-ch-ua': '"Chromium";v="95", ";Not A Brand";v="99"',
     'sec-ch-ua-mobile': '?1',
     'sec-ch-ua-model': '"22021211RG"',
     'sec-ch-ua-platform': '"Android"',
     'sec-ch-ua-platform-version': '"13.0.0"',
     'sec-fetch-dest': 'empty',
     'sec-fetch-mode': 'cors',
     'sec-fetch-site': 'same-origin',
     'user-agent': gg,
     'viewport-width': '391',
     'x-asbd-id': '129477',
     'x-csrftoken': 'OuvUFtGYLThj0EEZJg62u6bYHxbcXd4b',
     'x-ig-app-id': '1217981644879628',
     'x-ig-www-claim': '0',
     'x-instagram-ajax': '1009525636',
     'x-requested-with': 'XMLHttpRequest',
  } 
  data = {
     'email':email,
     }
  r=requests.post(url,headers=headers,data=data).text
  return r
@app.route('/')
def hello_world():
  return render_template('index.html', first_name="world", last_name="")
app.run(host='0.0.0.0', port=8080)