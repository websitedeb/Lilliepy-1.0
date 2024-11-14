from flask import Blueprint
from lilliepy_utils import render
from public.special import Layout, Not_Found

not_found_bp = Blueprint("errors", __name__)


@not_found_bp.app_errorhandler(404)
def not_found(err):
  return render(Not_Found(), title="404 ERROR", Layout=Layout), 404
