import flask
from flask_cors import CORS
from lilliepy_utils import initialize_app_data
from public.app import returnFavicon, returnMeta, returnTitle

initialize_app_data(returnFavicon, returnMeta, returnTitle)

server = flask.Flask(__name__,
                     static_folder="./public/assets",
                     template_folder="./public/views")

CORS(server)

export = server