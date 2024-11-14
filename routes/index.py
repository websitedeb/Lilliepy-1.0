from flask import Blueprint
from lilliepy_utils import render
from public.app import App
from public.special import Layout

index_bp = Blueprint("index", __name__)


@index_bp.route("/")
def index_func():
  return render(App(None), Layout)
