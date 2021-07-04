from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app

main = Blueprint('main', __name__, url_prefix='/')


@main.route('/main', methods=['GET'])
def index():
    return render_template('/main/index.html')


@main.route('/submit', methods=['GET', 'POST'])
def submit():
    return render_template('/submit.html')


@main.route('/list', methods=['GET'])
def get_list():
    return render_template('/list.html')
