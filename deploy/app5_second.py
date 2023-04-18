from flask import Flask, render_template, Blueprint

second =Blueprint("app5_second",__name__,static_folder='static',template_folder='template')

@second.route('/home')
def fun():
    return f'<h1>second home inside /next</h2>'
@second.route('/')
def home():
    return render_template("home.html")