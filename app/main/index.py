from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app

from app.module.dbModule import Database

main = Blueprint('main', __name__, url_prefix='/')


@main.route('/', methods=['GET'])
def index():
    return render_template('/main/index.html')


@main.route('/submit', methods=['POST'])
def submit():
    return render_template('/submit.html')


@main.route('/list', methods=['GET'])
def get_list():
    return render_template('/list.html')
