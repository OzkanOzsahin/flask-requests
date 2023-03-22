__winc_id__ = "cc1b724762854e85a8defa04287f708b"
__human_name__ = "requests"




from flask import Flask


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "<p>Home, sweet home.</p>"


@app.route("/greet/")
@app.route("/greet/<entity>", methods=["GET"])
def greet(entity="world"):
    return f"<h1>Hello, {entity}!</h1>"

#flask --app main run
#than run server: http://127.0.0.1:5000/greet/ or http://127.0.0.1:5000

if __name__ == '__main__':
    app.run()