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

        # form data preprocesscing
        writter = str(result.getlist("writter"))
        writter = writter[2:-2]
        description = str(result.getlist("description"))
        description = description[2:-2]

        # database insert query
        db = Database()
        sql = "INSERT INTO tellmeaboutme.list(writter, description, created) VALUES('%s', '%s', NOW())" % (
            writter, description)
        db.execute(sql)
        db.commit()

        return render_template('/submit.html', result=result)


@ main.route('/get_list', methods=['GET', 'POST'])
def get_list():

    if request.method == 'POST':

        result = request.form

        db = Database()
        sql = "SELECT * FROM tellmeaboutme.list"
        view = db.executeAll(sql)

        print(result)
        return render_template('/get_list.html', result=result)
