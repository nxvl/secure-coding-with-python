import sys

from flask import Blueprint, request, redirect, render_template, url_for

from marketplace.db import get_db

bp = Blueprint('listings', __name__, url_prefix='/listings')

@bp.route('/')
def index():
    cur = get_db().cursor()
    cur.execute(
        'SELECT id, title, description'
        ' FROM listings' 
    )
    listings = cur.fetchall()
    return render_template('listings/index.html', listings=listings)

@bp.route('/create', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        db = get_db()
        cur = db.cursor()

        sql = "INSERT INTO listings (title, description) VALUES ('%s', '%s')" % (title, description) 
        print(sql, file=sys.stdout)
        cur.execute(sql)
        db.commit()
        return redirect(url_for('listings.index'))

    return render_template('listings/create.html')

