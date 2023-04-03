from flask import Flask

app = Flask(__name__)

# hold a web server/ backend 
@app.route("/")
def hello_ghw():
    return "<p> Hello, API week hackers 2023 </p>"