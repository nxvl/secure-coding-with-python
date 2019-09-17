from flask import Blueprint, jsonify, json

from .models import Listing

bp = Blueprint('api_v1', __name__, url_prefix='/api/v1')


@bp.route('/listings', methods=('GET', ))
def listings():
    listings = Listing.query.all()
    ret = []
    for listing in listings:
        l = {
            "id": listing.id,
            "description": listing.description,
            "title": listing.title,
        }
        if listing.user:
            l["author"] = {
                "id": listing.user.full_name,
                "full_name": listing.user.full_name
            }
        ret.append(l)
    return json.dumps(ret)
