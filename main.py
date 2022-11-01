from flask import Flask, url_for

channel = ""
web = ""
UToken = ""
WToken = ""
app = Flask(__name__)

@app.route("/")
def home():
    return WToken
@app.route("/<name>")
def user(name):
    return f"Hello {name}! :)"
def channel():
   return WToken        
if __name__ == "__main__":
    app.run()


