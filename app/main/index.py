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


@main.route('/guestbook_list', methods=['GET', 'post'])
def guestbook_list():

    if request.method == 'GET':

        # database select query
        db = Database()
        sql = "SELECT * FROM tellmeaboutme.list"
        view = db.executeAll(sql)

        view_dict = {}

        # create dict using script
        for i in range(len(view)):

            view_dict[str(view[i]['id'])] = f"{view[i]['writter']}님의 게시물"

        return render_template('/guestbook_list.html', view_dict=view_dict)

    elif request.method == 'POST':

        # database select query
        db = Database()
        sql = "SELECT * FROM tellmeaboutme.list"
        view = db.executeAll(sql)

        view_dict = {}

        # create dict using script
        for i in range(len(view)):

            view_dict[str(view[i]['id'])] = f"{view[i]['writter']}님의 게시물"

        return render_template('/guestbook_list.html', view_dict=view_dict)


@main.route('/guestbook', methods=['GET', 'POST'])
def guestbook():

    # routed when you click '보기' button
    if request.method == 'POST':

        get_id = request.form
        get_id = str(get_id.getlist("id"))[2:-2]

        db = Database()
        sql = f"SELECT * FROM tellmeaboutme.list WHERE id={get_id}"
        view = db.executeOne(sql)

        return render_template('/guestbook.html', view=view, get_id=get_id)

    # routed when you clink anchor tag
    else:

        get_id = request.args.get('id')

        db = Database()
        sql = f"SELECT * FROM tellmeaboutme.list WHERE id={get_id}"
        view = db.executeOne(sql)

        return render_template('/guestbook.html', view=view, get_id=get_id)


@main.route('/guestbook/<int:id>', methods=['GET'])
def anchor_routing_guestbook(id):

    return redirect(url_for('main.guestbook', id=id))


@main.route('/delete', methods=["POST", "GET"])
def delete():

    get_id = request.args.get('id')

    db = Database()
    # database delete query
    delete_sql = f"DELETE FROM tellmeaboutme.list WHERE id={get_id}"
    db.execute(delete_sql)
    # database auto_increment(id value) rearrange query
    auto_increment_sql1 = "ALTER TABLE tellmeaboutme.list AUTO_INCREMENT=1"
    db.execute(auto_increment_sql1)
    auto_increment_sql2 = "SET @count = 0"
    db.execute(auto_increment_sql2)
    auto_increment_sql3 = "UPDATE tellmeaboutme.list SET id = @count:=@count+1"
    db.execute(auto_increment_sql3)
    db.commit()

    return redirect(url_for('main.guestbook_list'))


@main.route('/divide_method', methods=["POST"])
def divide_method():

    _method = request.form['_method']
    id = request.form['id']

    if _method == "delete":
        return redirect(url_for('main.delete', id=id))
    else:
        return 0


@main.route('/password', methods=["POST"])
def password():

    _method = request.form['_method']
    get_id = request.form['id']

    return render_template('/checkpassword.html', _method=_method, get_id=get_id)
