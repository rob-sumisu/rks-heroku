from flask import Flask
app = Flask(__name__)
import time

@app.route('/')
def index():
  localtime = time.localtime(time.time())
  return '<b>hello heroku - My updated 2:51 </b> branch 1'

  
  
