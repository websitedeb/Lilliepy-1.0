from flask import Blueprint, request
from lilliepy_utils import render
from public.app import App
from public.special import Layout, Error

vars_bp = Blueprint("vars", __name__)


@vars_bp.route("/name")
def vars_func():
  params = request.args.to_dict()
  if params:
    return render(App(params), Layout)
  else:
    return render(Error("Requires variable", 404),
                  title="Invalid Request",
                  Layout=Layout)
