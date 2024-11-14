from .index import index_bp
from .dynamic import dynamic_bp
from .error import not_found_bp
from .vars import vars_bp


def blueprints(app):
  app.register_blueprint(index_bp)
  app.register_blueprint(dynamic_bp)
  app.register_blueprint(vars_bp)
  app.register_blueprint(not_found_bp)
