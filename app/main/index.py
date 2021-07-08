from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app

from app.module.dbModule import Database

main = Blueprint('main', __name__, url_prefix='/')


@main.route('/', methods=['GET'])
def index():
    return render_template('/main/index.html')


@main.route('/submit', methods=['POST'])
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

        return render_template('/submit.html')


@main.route('/get_list', methods=['POST'])
def get_list():

    if request.method == 'POST':

        # database select query
        db = Database()
        sql = "SELECT * FROM tellmeaboutme.list"
        view = db.executeAll(sql)

        view_dict = {}

        # create dict using script
        for i in range(len(view)):

            view_dict[str(view[i]['id'])] = f"{view[i]['writter']}님의 게시물"

        return render_template('/get_list.html', view_dict=view_dict)


@main.route('/visit', methods=['GET', 'POST'])
def visit():

    # routed when you click '보기' button
    if request.method == 'POST':

        get_id = request.form
        get_id = str(get_id.getlist("id"))[2:-2]

        db = Database()
        sql = f"SELECT * FROM tellmeaboutme.list WHERE id={get_id}"
        view = db.executeOne(sql)

        return render_template('/visit.html', view=view)

    # routed when you clink anchor tag
    else:

        get_id = request.args.get('id')

        db = Database()
        sql = f"SELECT * FROM tellmeaboutme.list WHERE id={get_id}"
        view = db.executeOne(sql)

        return render_template('/visit.html', view=view)


@main.route('/visit/<int:id>', methods=['GET'])
def anchor_routing_visit(id):

    return redirect(url_for('main.visit', id=id))
