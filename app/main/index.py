from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app

from app.module.dbModule import Database

main = Blueprint('main', __name__, url_prefix='/')


@main.route('/', methods=['GET'])
def index():
    return render_template('/main/index.html')


@main.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        result = request.form
        print(result)
        return render_template('/submit.html', result=result)


@main.route('/get_list', methods=['GET', 'POST'])
def get_list():
    if request.method == 'POST':
        result = request.form
        print(result)
        return render_template('/get_list.html', result=result)
