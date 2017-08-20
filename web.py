from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  localtime = time.localtime(time.time())
  return '<b>hello heroku</b> ' + localtime

  
  
