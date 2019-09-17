from flask import Blueprint, jsonify, json

from .models import Listing

bp = Blueprint('api_v1', __name__, url_prefix='/api/v1')


def to_dict(obj):
    if obj is None:
        return obj

    ret = {}
    for c in obj.__table__.columns:
        if c.name[-3:] == "_id":
            key = c.name[:-3]
            ret[key] = to_dict(getattr(obj, key))
        else:
            ret[c.name] = getattr(obj, c.name)
    return ret


@bp.route('/listings', methods=('GET', ))
def listings():
    listings = Listing.query.all()
    return json.dumps([to_dict(l) for l in listings])
