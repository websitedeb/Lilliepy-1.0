from routes import blueprints
from config import export as server

blueprints(server)

if __name__ == "__main__":
  server.run(host="0.0.0.0", port=8080)
