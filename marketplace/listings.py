import sys
 
from flask import Blueprint, request, redirect, render_template, url_for, abort

from . import db
from .helpers import auth
from .models import Listing
 
bp = Blueprint('listings', __name__, url_prefix='/listings')


@bp.route('/')
def index():
    listings = Listing.query.all()
    return render_template('listings/index.html', listings=listings)


@bp.route('/create', methods=('GET', 'POST'))
@auth
def register(user):
    if request.method == 'POST':
        listing = Listing(
            title=request.form['title'],
            description=request.form['description'],
            user=user,
        )
        db.session.add(listing)
        db.session.commit()

        return redirect(url_for('listings.index'))

    return render_template('listings/create.html')


@bp.route('/<int:listing_id>', methods=('GET', 'POST'))
@auth
def edit_listing(user, listing_id):
    listing = db.session.query(Listing).filter_by(id=listing_id, user=user).scalar()
    if not listing:
        return abort(404)
    if request.method == 'POST':
        listing.title = request.form['title']
        listing.description = request.form['description']
        db.session.commit()
    return render_template('listings/edit.html', user=user, listing=listing)
