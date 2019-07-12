from flask import url_for, render_template, Blueprint, flash, request, redirect

core = Blueprint('core', __name__)

@core.route("/")
def index():
	return render_template("index.html")

@core.route("/info")
def info():
	return render_template('info.html')