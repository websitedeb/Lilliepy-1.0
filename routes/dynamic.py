from flask import Blueprint, request
from lilliepy_utils import render
from public.app import App
from public.special import Layout, Error

dynamic_bp = Blueprint("dynamic", __name__)


@dynamic_bp.route("/<var>")
def dynamic_func(var):
  if var:
    return render(App(var), Layout)
  else:
    return render(Error("Invalid variable", 404),
                  title="Invalid Request",
                  Layout=Layout)
