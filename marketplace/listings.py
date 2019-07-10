import sys
 
from flask import Blueprint, request, redirect, render_template, url_for
 
from . import db
from .models import Listing
 
bp = Blueprint('listings', __name__, url_prefix='/listings')
 
@bp.route('/')
def index():
    listings = Listing.query.all()
    return render_template('listings/index.html', listings=listings)

@bp.route('/create', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        listing = Listing(title=request.form['title'], description=request.form['description'])
        db.session.add(listing)
        db.session.commit()

        return redirect(url_for('listings.index'))

    return render_template('listings/create.html')

