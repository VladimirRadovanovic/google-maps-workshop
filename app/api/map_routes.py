from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Listing
import os
from sqlalchemy import text

map_routes = Blueprint('map', __name__)


@map_routes.route('/key', methods=['POST'])
@login_required
def load_map_key():
    key = os.environ.get('MAPS_API_KEY')
    return {'googleMapsAPIKey': key}


@map_routes.route('/<string:address>/<string:lat>/<string:lng>')
@login_required
def get_places(address, lat, lng):
    print(address, lat, lng, '/n/n!!!!!!!!!!!!!!!!!!!/n/n')

    parsed_city = address[:-9]
    distance = 20

    if ',' in parsed_city:
        i = parsed_city.index(',')
        parsed_city = parsed_city[i+2:]

    # places = Listing.query.filter(Listing.city == parsed_city).all()

    clause = "SQRT(POW(69.1 * (lat - :lati),2) + POW(53.0 * (lng - :long),2)) < :dis"
# query = meta.Session.query(User).filter(clause).params(lat=my_latitude, long=my_longitude)

    places = Listing.query.filter(text(clause)).params(lati=lat, long=lng, dis=distance).all()

    # places = Listing.execute()

    print(places, '\n!!!!!!!!!!!!!!!!!!!!\n\n')


    return {'places': [place.to_dict() for place in places]}
