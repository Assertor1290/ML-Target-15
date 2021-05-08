from flask import Flask, request
app = Flask("Assertor")
@app.route("/home/")
def hello():
    return str(request.args)
app.run()