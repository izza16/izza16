
from flask import Flask, render_template, request
application = Flask(__name__)
@application.route("/")
def index():
    return render_template("kamyab.html")


@application.route("/ok.py/",methods=["POST"])
def fun():
        first = request.form['fname']
        second = request.form['lname']
        third = request.form['tname']
        name1= int(first)+int(second)

        name = name1/int(third)
        return render_template("kamyab.html",results=name)
if __name__ == '__main__':
    application.run(host="localhost",port=8081)



