from flask import Flask
app = Flask(__name__)
import time

@app.route('/')
def index():
  localtime = time.localtime(time.time())
  return '<b>hello heroku</b> branch 1'

  
  
