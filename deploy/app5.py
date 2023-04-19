# is for blueprint and linking multiple files
from flask import Flask, render_template, Blueprint
from app5_second import second

app5 = Flask(__name__, static_folder='static', template_folder='template')
app5.register_blueprint(second, url_prefix='/next')


@app5.route("/home")
def fun():
    return f'<h1> first home  </h1>'


@app5.route("/")
def home():
    return f'<h1> first </h1>'


@app5.route("/video")
def vid():
    return render_template("video.html")


if __name__ == "__main__":
    app5.run(debug=True,host='0.0.0.0',port=5001)
